# llm_benchmark
自己用的模型基准测试

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行基准测试

默认情况下会读取 `configs.yaml` 中全部模型配置并对 `prompts.py` 中的测试用例运行 3 轮基准测试：

```bash
python model_benchmark.py
```

常用参数：

* `--models`：指定要测试的模型键，多个模型使用逗号分隔，例如 `--models Qwen_Qwen3-30B-A3B-FP8,Qwen_Qwen3-32B-AWQ`
* `--runs`：每条提示词运行次数，默认 3 次
* `--output`：结果 CSV 文件名，默认自动生成（示例：`benchmark_results_20250724_173718.csv`）
* `--config`：自定义配置文件路径，默认 `configs.yaml`

完整示例：

```bash
python model_benchmark.py --models Qwen_Qwen3-30B-A3B-FP8 --runs 5 --output result.csv
```

## 配置文件说明（`configs.yaml`）

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
