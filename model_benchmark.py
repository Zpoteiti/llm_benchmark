#!/usr/bin/env python3
"""
LLM Model Streaming Benchmark Tool
Tests streaming output speed, token length, and performance metrics for different models.
"""

import time
import csv
import statistics
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import argparse
import sys
from openai import OpenAI

# 导入配置和提示词
from configs import ConfigLoader, ModelConfig
from prompts import test_prompts, SYSTEM_PROMPT


@dataclass
class BenchmarkResult:
    """Results from a single benchmark run."""
    model_name: str
    prompt_tokens: int
    response_tokens: int
    total_tokens: int
    # 时间指标
    total_time: float  # 总时间
    preprocess_time: Optional[float] = None  # 预处理时间
    generation_time: Optional[float] = None  # 纯生成时间
    # 速度指标
    total_tokens_per_second: float = 0
    preprocess_speed: Optional[float] = None  # input tokens / preprocess time
    generation_speed: Optional[float] = None  # response tokens / generation time
    # 其他指标
    timestamp: str = ""
    success: bool = False
    error_message: Optional[str] = None
    streaming_used: bool = True  # 固定为流式输出


class ModelBenchmark:
    """Main benchmark class for testing LLM models."""
    
    def __init__(self, config_loader: ConfigLoader):
        self.config_loader = config_loader
        self.results: List[BenchmarkResult] = []
        
        # 从prompts.py加载测试提示词
        self.test_prompts = test_prompts
    
    def get_model_configs(self) -> Dict[str, Any]:
        """Get configurations for all available models from configs.yaml."""
        return self.config_loader.get_model_configs()
    
    def create_client(self, config: Any) -> OpenAI:
        """Create OpenAI client for a specific model."""
        return OpenAI(
            base_url=f"{config.base_url}:{config.port}/v1",
            api_key="dummy_key"  # Most local deployments don't require real API keys
        )
    
    def run_single_test(self, config: Any, prompt: str, run_number: int) -> BenchmarkResult:
        """Run a single streaming benchmark test for a model."""
        client = self.create_client(config)
        
        model = config.model_name
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        temperature = config.temperature
        max_tokens = config.max_tokens if config.max_tokens else 1024
        extra_body = config.extra_body if config.extra_body else {}
        
        start_time = time.time()
        
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                extra_body=extra_body,
                stream=True,
                stream_options={"include_usage": True}
            )
            
            first_chunk_time = None
            response_content = ""
            usage_info = None
            
            for chunk in response:
                current_time = time.time()
                
                if first_chunk_time is None:
                    first_chunk_time = current_time
                
                if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                    response_content += chunk.choices[0].delta.content
                
                # 尝试获取usage信息（某些API在最后的chunk中包含usage）
                if hasattr(chunk, 'usage') and chunk.usage:
                    usage_info = chunk.usage
            
            end_time = time.time()
            
            # 计算时间指标
            total_time = end_time - start_time
            preprocess_time = first_chunk_time - start_time if first_chunk_time else total_time
            generation_time = end_time - first_chunk_time if first_chunk_time else 0
            
            # 获取token数量 - 优先使用API返回的精确值
            if usage_info:
                prompt_tokens = usage_info.prompt_tokens
                response_tokens = usage_info.completion_tokens
                total_tokens = usage_info.total_tokens
                print(f"prompt_tokens: {prompt_tokens}, response_tokens: {response_tokens}, total_tokens: {total_tokens}")
            
            # 计算速度指标
            total_tokens_per_second = total_tokens / total_time if total_time > 0 else 0
            preprocess_speed = prompt_tokens / preprocess_time if preprocess_time > 0 else 0
            generation_speed = response_tokens / generation_time if generation_time > 0 else 0
            
            return BenchmarkResult(
                model_name=config.name,
                prompt_tokens=prompt_tokens,
                response_tokens=response_tokens,
                total_tokens=total_tokens,
                total_time=total_time,
                preprocess_time=preprocess_time,
                generation_time=generation_time,
                total_tokens_per_second=total_tokens_per_second,
                preprocess_speed=preprocess_speed,
                generation_speed=generation_speed,
                timestamp=datetime.now().isoformat(),
                success=True,
                streaming_used=True
            )
                
        except Exception as e:
            end_time = time.time()
            return BenchmarkResult(
                model_name=config.name,
                prompt_tokens=len(prompt),  # 错误情况下的估算
                response_tokens=0,
                total_tokens=0,
                total_time=end_time - start_time,
                timestamp=datetime.now().isoformat(),
                success=False,
                error_message=str(e),
                streaming_used=True
            )
    

    
    def run_benchmark(self, model_keys: Optional[List[str]] = None, runs_per_prompt: int = 3) -> None:
        """Run streaming benchmark tests for specified models."""
        model_configs = self.get_model_configs()
        
        # 如果未指定模型，测试所有模型
        if not model_keys:
            model_keys = list(model_configs.keys())
        
        # 验证模型是否存在
        valid_model_keys = []
        for key in model_keys:
            if key in model_configs:
                valid_model_keys.append(key)
            else:
                print(f"Warning: Model '{key}' not found in configurations")
        
        if not valid_model_keys:
            print("Error: No valid models specified")
            return
        
        print(f"Starting streaming benchmark with {len(valid_model_keys)} models, {runs_per_prompt} runs per prompt")
        
        # 对每个模型运行测试
        for model_key in valid_model_keys:
            config = model_configs[model_key]
            print(f"\nTesting {config.name}...")
            
            # 对每个提示词运行多次测试
            for prompt_idx, prompt in enumerate(self.test_prompts):
                print(f"  Prompt {prompt_idx + 1}/{len(self.test_prompts)}")
                
                for run in range(runs_per_prompt):
                    print(f"    Run {run + 1}/{runs_per_prompt}")
                    result = self.run_single_test(config, prompt, run)
                    self.results.append(result)
                    
                    if result.success:
                        print(f"      Success: {result.total_tokens_per_second:.2f} total tokens/sec, "
                              f"{result.generation_speed:.2f} generation tokens/sec, "
                              f"{result.preprocess_speed:.1f} preprocess tokens/sec")
                    else:
                        print(f"      Failed: {result.error_message}")
    
    def save_results_to_csv(self, output_file: str = None) -> None:
        """Save benchmark results to CSV file."""
        if not self.results:
            print("No results to save")
            return
        
        # 如果未指定输出文件，生成一个包含时间戳的文件名
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"benchmark_results_{timestamp}.csv"
        
        # 写入CSV文件
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'model_name', 'prompt_tokens', 'response_tokens', 'total_tokens',
                'total_time', 'preprocess_time', 'generation_time',
                'total_tokens_per_second', 'preprocess_speed', 'generation_speed', 
                'timestamp', 'success', 'error_message', 'streaming_used'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for result in self.results:
                writer.writerow({
                    'model_name': result.model_name,
                    'prompt_tokens': result.prompt_tokens,
                    'response_tokens': result.response_tokens,
                    'total_tokens': result.total_tokens,
                    'total_time': result.total_time,
                    'preprocess_time': result.preprocess_time,
                    'generation_time': result.generation_time,
                    'total_tokens_per_second': result.total_tokens_per_second,
                    'preprocess_speed': result.preprocess_speed,
                    'generation_speed': result.generation_speed,
                    'timestamp': result.timestamp,
                    'success': result.success,
                    'error_message': result.error_message,
                    'streaming_used': result.streaming_used
                })
        
        print(f"Results saved to {output_file}")
    
    def generate_summary(self) -> None:
        """Generate and print a summary of benchmark results."""
        if not self.results:
            print("No results to summarize")
            return
        
        print("\n" + "=" * 80)
        print("BENCHMARK SUMMARY")
        print("=" * 80)
        print(f"Total results collected: {len(self.results)}")
        
        # 按模型分组结果
        model_results = {}
        for result in self.results:
            if result.model_name not in model_results:
                model_results[result.model_name] = []
            model_results[result.model_name].append(result)
        
        print(f"Models tested: {len(model_results)}")
        print()
        
        # 计算每个模型的统计数据
        performance_data = []
        
        for model_name, results in model_results.items():
            successful = [r for r in results if r.success]
            failed = [r for r in results if not r.success]
            
            print(f"{model_name}:")
            print(f"  Successful tests: {len(successful)}")
            print(f"  Failed tests: {len(failed)}")
            
            if successful:
                total_tps_values = [r.total_tokens_per_second for r in successful]
                tokens_per_response = [r.response_tokens for r in successful]
                preprocess_times = [r.preprocess_time for r in successful if r.preprocess_time]
                generation_times = [r.generation_time for r in successful if r.generation_time]
                preprocess_speeds = [r.preprocess_speed for r in successful if r.preprocess_speed]
                generation_speeds = [r.generation_speed for r in successful if r.generation_speed]
                
                print(f"  Average total tokens/sec: {statistics.mean(total_tps_values):.2f}")
                print(f"  Median total tokens/sec: {statistics.median(total_tps_values):.2f}")
                print(f"  Max total tokens/sec: {max(total_tps_values):.2f}")
                print(f"  Average tokens per response: {statistics.mean(tokens_per_response):.1f}")
                
                # 显示详细时间指标
                if preprocess_times:
                    print(f"  Average preprocess time: {statistics.mean(preprocess_times)*1000:.1f}ms")
                    print(f"  Average generation time: {statistics.mean(generation_times)*1000:.1f}ms")
                if preprocess_speeds:
                    print(f"  Average preprocess speed: {statistics.mean(preprocess_speeds):.1f} tokens/sec")
                if generation_speeds:
                    print(f"  Average generation speed: {statistics.mean(generation_speeds):.1f} tokens/sec")
                
                # 使用generation speed作为主要性能指标进行排名
                if generation_speeds:
                    avg_generation_speed = statistics.mean(generation_speeds)
                    performance_data.append((model_name, avg_generation_speed))
            
            print()
        
        # 按性能排序并显示
        if performance_data:
            print("=" * 80)
            print("PERFORMANCE RANKING")
            print("=" * 80)
            
            # 按性能指标降序排序
            performance_data.sort(key=lambda x: x[1], reverse=True)
            
            for i, (model_name, avg_speed) in enumerate(performance_data, 1):
                print(f"{i}. {model_name}: {avg_speed:.2f} generation tokens/sec")
        
        print("=" * 80)


def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='LLM Model Streaming Benchmark Tool')
    parser.add_argument('--models', help='Models to benchmark (comma-separated, default: all)')
    parser.add_argument('--runs', type=int, default=3, help='Runs per prompt (default: 3)')
    parser.add_argument('--output', help='Output CSV filename (default: auto-generated)')
    parser.add_argument('--config', default='configs.yaml', help='Path to config file (default: configs.yaml)')
    args = parser.parse_args()
    
    try:
        # 加载配置
        config_loader = ConfigLoader(args.config)
        
        # 创建基准测试实例
        benchmark = ModelBenchmark(config_loader)
        
        # 处理模型列表（支持逗号分隔）
        model_keys = None
        if args.models:
            model_keys = [model.strip() for model in args.models.split(',')]
        
        # 运行基准测试
        benchmark.run_benchmark(model_keys=model_keys, runs_per_prompt=args.runs)
        
        # 保存结果
        benchmark.save_results_to_csv(args.output)
        
        # 生成摘要
        benchmark.generate_summary()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()