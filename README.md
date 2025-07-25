# LLM Model Benchmark Tool

这是一个用于测试和比较不同LLM模型性能的工具，特别关注输出速度、token长度和响应时间等指标。

## 新功能：详细时间分析

### 时间计算改进

程序现在支持更详细的时间分析，可以区分：

- **预处理时间** (`preprocess_time`): 模型处理输入并开始生成第一个token的时间
- **生成时间** (`generation_time`): 从第一个token到完成输出的时间  
- **总时间** (`total_time`): 完整的请求-响应时间

### 速度指标

- **预处理速度** (`preprocess_speed`): `input_tokens / preprocess_time` (tokens/sec)
- **生成速度** (`generation_speed`): `response_tokens / generation_time` (tokens/sec)
- **总token速度** (`total_tokens_per_second`): `total_tokens / total_time` (tokens/sec)
- **响应token速度** (`response_tokens_per_second`): `response_tokens / total_time` (tokens/sec)

### 流式 vs 非流式模式

#### 流式模式（默认，推荐）
- 使用 `stream=True` 参数
- 能够准确测量预处理时间（到首个token的时间）和生成时间
- 提供最精确的时间分解

#### 非流式模式
- 使用 `--no-streaming` 参数启用
- 只能测量总时间
- 预处理时间和生成时间基于经验估算（预处理占总时间的10%）

## 使用方法

### 基本用法

```bash
# 使用流式模式测试所有模型（推荐）
python3 model_benchmark.py

# 使用非流式模式
python3 model_benchmark.py --no-streaming

# 测试特定模型
python3 model_benchmark.py --models "model1,model2"

# 指定测试次数
python3 model_benchmark.py --runs 5
```

### 命令行参数

- `--models MODELS`: 要测试的模型（逗号分隔，默认：全部）
- `--runs RUNS`: 每个提示词的运行次数（默认：3）
- `--output OUTPUT`: 输出CSV文件名（默认：自动生成）
- `--config CONFIG`: 配置文件路径（默认：configs.yaml）
- `--no-streaming`: 禁用流式模式（默认启用流式）

## 输出指标说明

### CSV输出字段

- `model_name`: 模型名称
- `prompt_tokens`: 输入token数
- `response_tokens`: 响应token数  
- `total_tokens`: 总token数
- `total_time`: 总时间（秒）
- `preprocess_time`: 预处理时间（秒）
- `first_token_time`: 首个token时间（秒）
- `generation_time`: 生成时间（秒）
- `total_tokens_per_second`: 总token速度
- `response_tokens_per_second`: 响应token速度
- `preprocess_speed`: 预处理速度（tokens/sec）
- `generation_speed`: 生成速度（tokens/sec）
- `latency`: 延迟（流式：首个token时间，非流式：总时间）
- `timestamp`: 时间戳
- `success`: 是否成功
- `error_message`: 错误信息
- `streaming_used`: 是否使用了流式模式

### 性能排名

程序会根据以下指标进行性能排名：
- **流式结果**: 使用 `generation_speed` (生成速度)
- **非流式结果**: 使用 `response_tokens_per_second` (响应token速度)

## 配置文件

```yaml
models:
  Qwen_Qwen3-30B-A3B-FP8:
    base_url: "http://10.180.116.2"
    port: 6384
    temperature: 0.7
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
* `max_tokens`：生成最大 token 数，默认 `None`（由服务端决定）
* `extra_body`：透传给 `/chat/completions` 的自定义字段，底层通过 `extra_body` 发送

### 1. CSV报告
测试结果会保存为CSV文件，包含以下字段：
- `model_name`: 模型名称
- `prompt_tokens`: 输入提示词的token数量
- `response_tokens`: 模型响应的token数量
- `total_tokens`: 总token数（输入+输出）
- `generation_time`: 生成时间（秒）
- `total_tokens_per_second`: 总token生成速度（包含输入处理时间）
- `response_tokens_per_second`: 响应token生成速度（纯输出速度）
- `latency`: 延迟
- `timestamp`: 时间戳
- `success`: 是否成功
- `error_message`: 错误信息（如有）

### 2. 控制台摘要
程序会在控制台输出详细的统计摘要，包括：
- 各模型的成功/失败测试数量
- 平均、中位数、最大总token生成率和响应token生成率
- 平均延迟和响应token数量
- 基于响应token生成速度的性能排名

## 变更记录

* **2025-07-24**：
  * 修复 `extra_body` 参数会导致未知关键字错误的问题，现通过官方 `extra_body` 机制传递
  * 更新依赖版本（`openai>=1.6.1`, `PyYAML>=6.0`）
  * 完善 README，增加安装、使用说明以及配置字段解释
