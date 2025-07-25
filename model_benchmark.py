#!/usr/bin/env python3
"""
LLM Model Benchmark Tool
Tests output speed, token length, and performance metrics for different models.
"""

import time
import csv
import json
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
    generation_time: float
    total_tokens_per_second: float
    response_tokens_per_second: float
    latency: float
    timestamp: str
    success: bool
    error_message: Optional[str] = None


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
        """Run a single benchmark test for a model."""
        client = self.create_client(config)
        
        start_time = time.time()
        
        try:
            
            model = config.model_name
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
            temperature = config.temperature
            max_tokens = config.max_tokens if config.max_tokens else 1024
            # 使用配置中的extra_body，如果没有则为空字典
            extra_body = config.extra_body if config.extra_body else {}
            
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                extra_body=extra_body
            )
            
            end_time = time.time()
            generation_time = end_time - start_time
            
            # 计算指标 - 使用API返回的真实token数量
            response_content = response.choices[0].message.content or ""
            
            # 优先使用API返回的精确token数，如果没有则回退到字符数估算
            if response.usage:
                prompt_tokens = response.usage.prompt_tokens
                response_tokens = response.usage.completion_tokens
                total_tokens = response.usage.total_tokens
                print(f"prompt_tokens: {prompt_tokens}, response_tokens: {response_tokens}, total_tokens: {total_tokens}")
            # else:
            #     # 回退到字符数估算（不准确，但总比没有好）
            #     print("response.usage is None, falling back to character count")
            #     prompt_tokens = len(messages[1]['content'])
            #     response_tokens = len(response_content)
            #     total_tokens = prompt_tokens + response_tokens
            
            # 计算两种token速度指标
            total_tokens_per_second = total_tokens / generation_time if total_tokens > 0 else 0
            response_tokens_per_second = response_tokens / generation_time if response_tokens > 0 else 0
            latency = generation_time
            
            return BenchmarkResult(
                model_name=config.name,
                prompt_tokens=prompt_tokens,
                response_tokens=response_tokens,
                total_tokens=total_tokens,
                generation_time=generation_time,
                total_tokens_per_second=total_tokens_per_second,
                response_tokens_per_second=response_tokens_per_second,
                latency=latency,
                timestamp=datetime.now().isoformat(),
                success=True
            )
        except Exception as e:
            end_time = time.time()
            return BenchmarkResult(
                model_name=config.name,
                prompt_tokens=len(prompt),  # 错误情况下的估算
                response_tokens=0,
                total_tokens=0,
                generation_time=end_time - start_time,
                total_tokens_per_second=0,
                response_tokens_per_second=0,
                latency=end_time - start_time,
                timestamp=datetime.now().isoformat(),
                success=False,
                error_message=str(e)
            )
    
    def run_benchmark(self, model_keys: Optional[List[str]] = None, runs_per_prompt: int = 3) -> None:
        """Run benchmark tests for specified models."""
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
        
        print(f"Starting benchmark with {len(valid_model_keys)} models, {runs_per_prompt} runs per prompt")
        
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
                        print(f"      Success: {result.total_tokens_per_second:.2f} tokens/sec")
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
                'generation_time', 'total_tokens_per_second', 'response_tokens_per_second', 'latency', 'timestamp',
                'success', 'error_message'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for result in self.results:
                writer.writerow({
                    'model_name': result.model_name,
                    'prompt_tokens': result.prompt_tokens,
                    'response_tokens': result.response_tokens,
                    'total_tokens': result.total_tokens,
                    'generation_time': result.generation_time,
                    'total_tokens_per_second': result.total_tokens_per_second,
                    'response_tokens_per_second': result.response_tokens_per_second,
                    'latency': result.latency,
                    'timestamp': result.timestamp,
                    'success': result.success,
                    'error_message': result.error_message
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
                response_tps_values = [r.response_tokens_per_second for r in successful]
                latency_values = [r.latency for r in successful]
                tokens_per_response = [r.response_tokens for r in successful]
                
                print(f"  Average total tokens/sec: {statistics.mean(total_tps_values):.2f}")
                print(f"  Average response tokens/sec: {statistics.mean(response_tps_values):.2f}")
                print(f"  Median total tokens/sec: {statistics.median(total_tps_values):.2f}")
                print(f"  Median response tokens/sec: {statistics.median(response_tps_values):.2f}")
                print(f"  Max total tokens/sec: {max(total_tps_values):.2f}")
                print(f"  Max response tokens/sec: {max(response_tps_values):.2f}")
                print(f"  Average latency: {statistics.mean(latency_values):.2f}s")
                print(f"  Average tokens per response: {statistics.mean(tokens_per_response):.1f}")
                
                # 使用response tokens/sec作为主要性能指标进行排名
                performance_data.append((model_name, statistics.mean(response_tps_values)))
            
            print()
        
        # 按性能排序并显示
        if performance_data:
            print("=" * 80)
            print("PERFORMANCE RANKING (by Response Tokens/sec)")
            print("=" * 80)
            
            # 按response tokens/sec降序排序
            performance_data.sort(key=lambda x: x[1], reverse=True)
            
            for i, (model_name, avg_response_tps) in enumerate(performance_data, 1):
                print(f"{i}. {model_name}: {avg_response_tps:.2f} response tokens/sec")
        
        print("=" * 80)


def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='LLM Model Benchmark Tool')
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