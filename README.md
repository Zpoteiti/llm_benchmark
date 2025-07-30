# LLM Model Streaming Benchmark Tool

这是一个专门用于测试LLM模型流式输出性能的工具，专注于准确测量输出速度、token长度和响应时间等关键指标。

## 核心功能：精确的流式性能测试

### 时间分析指标

程序通过流式输出提供精确的时间分解：

- **预处理时间** (`preprocess_time`): 模型处理输入并开始生成第一个token的时间
- **生成时间** (`generation_time`): 从第一个token到完成输出的纯生成时间  
- **总时间** (`total_time`): 完整的请求-响应时间

### 速度指标

- **预处理速度** (`preprocess_speed`): `prompt_tokens / preprocess_time` (tokens/sec)
- **生成速度** (`generation_speed`): `response_tokens / generation_time` (tokens/sec) - **核心性能指标**
- **总token速度** (`total_tokens_per_second`): `total_tokens / total_time` (tokens/sec)

### 流式输出优势

- **精确时间测量**: 能够准确区分预处理和生成阶段
- **实时性能**: 测量真实的token生成速度
- **详细分析**: 提供完整的性能分解数据
- **自动获取用量**: 通过 `stream_options={"include_usage": True}` 获取精确的token统计
- **热身机制**: 自动执行热身测试消除首次运行的缓存影响

## 使用方法

### 基本用法

```bash
# 测试所有模型
python model_benchmark.py

# 测试特定模型
python model_benchmark.py --models "model1,model2"

# 指定测试次数
python model_benchmark.py --runs 5

# 指定输出文件
python model_benchmark.py --output my_results.csv

# 自用示例
python model_benchmark.py --output H20-Qwen_Qwen3-30B-A3B-GPTQ-Int4-yarn.csv --runs 1

# 禁用热身测试
python model_benchmark.py --no-warmup
```

### 命令行参数

- `--models MODELS`: 要测试的模型（逗号分隔，默认：全部）
- `--runs RUNS`: 每个提示词的运行次数（默认：3）
- `--output OUTPUT`: 输出CSV文件名（默认：自动生成）
- `--config CONFIG`: 配置文件路径（默认：configs.yaml）
- `--no-warmup`: 禁用热身测试（默认：启用热身）

## 输出指标说明

### CSV输出字段

- `model_name`: 模型名称
- `prompt_tokens`: 输入token数
- `response_tokens`: 响应token数  
- `total_tokens`: 总token数
- `total_time`: 总时间（秒）
- `preprocess_time`: 预处理时间（秒）
- `generation_time`: 生成时间（秒）
- `total_tokens_per_second`: 总token速度
- `preprocess_speed`: 预处理速度（tokens/sec）
- `generation_speed`: 生成速度（tokens/sec）- **主要性能指标**
- `timestamp`: 时间戳
- `success`: 是否成功
- `error_message`: 错误信息
- `streaming_used`: 是否使用了流式模式（固定为true）

### 控制台输出示例

```
Testing Qwen_Qwen3-30B-A3B-GPTQ-Int4...
  Warmup...
    Warmup completed: 85.2 generation tokens/sec
  Prompt 1/10
    Run 1/3
      Success: 11470.01 total tokens/sec, 87.0 generation tokens/sec, 135981.1 preprocess tokens/sec
```

### 性能排名

程序根据 `generation_speed`（纯生成速度）进行性能排名，这是最准确反映模型推理性能的指标。

## 配置文件

```yaml
models:
  Qwen_Qwen3-30B-A3B-GPTQ-Int4:
    base_url: "http://10.180.116.2"
    port: 6384
    model_name: "Qwen3-30B-A3B-GPTQ-Int4"
    temperature: 0.7
    max_tokens: 1024
    # 其他自定义请求体参数可放在 extra_body 中
    extra_body:
      chat_template_kwargs:
        enable_thinking: false
```

### 字段含义

* `base_url`：模型服务的基础地址，必须包含协议 (`http://` 或 `https://`)
* `port`：服务端口
* `name`：可选，模型在报告中的展示名称，默认使用配置键
* `model_name`：可选，发送给接口的模型名称，默认使用配置键
* `temperature`：采样温度，默认 `0.7`
* `max_tokens`：生成最大 token 数，默认 `1024`
* `extra_body`：透传给 `/chat/completions` 的自定义字段

## 技术特性

### 流式输出配置

程序自动配置流式输出以获得最佳性能数据：

```python
stream=True,
stream_options={"include_usage": True}
```

### 精确Token统计

- **使用API返回值**: 通过 `stream_options={"include_usage": True}` 获取精确的token统计
- **保证数据准确性**: 依赖API提供的准确token计数，无需估算
- **完整错误处理**: robust的异常处理确保测试稳定性

### 热身机制

- **自动热身**: 每个模型测试前自动执行一次热身请求
- **消除冷启动影响**: 预热模型缓存、GPU内存、连接池等
- **简短热身提示**: 使用 "Hello, how are you?" 进行快速热身
- **可选配置**: 通过 `--no-warmup` 参数可以禁用热身功能

### 输出报告

1. **CSV详细数据**: 包含所有性能指标的详细数据
2. **控制台摘要**: 实时显示测试进度和关键指标
3. **性能排名**: 基于生成速度的模型性能排序

## 安装依赖

```bash
pip install openai>=1.6.1 PyYAML>=6.0
```

或者使用requirements.txt:

```bash
pip install -r requirements.txt
```