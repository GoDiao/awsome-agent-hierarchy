# Awesome AI Agent 全栈框架 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

AI Agent 系统构建工具、库、框架和资源的精选列表，按架构层级分类整理。

> **声明：** 本列表正在持续建设中，欢迎贡献！

## 目录

- [01. 基础层](#01-基础层)
  - [大语言模型](#大语言模型)
  - [提示工程](#提示工程)
  - [上下文](#上下文)
- [02. 代理大脑](#02-代理大脑)
  - [规划](#规划)
  - [推理](#推理)
  - [决策引擎](#决策引擎)
- [03. 工具层](#03-工具层)
- [04. 代理工作流](#04-代理工作流)
- [05. 多代理系统](#05-多代理系统)
- [06. 基础设施](#06-基础设施)
- [07. 可观测性](#07-可观测性)
- [08. 安全层](#08-安全层)
- [贡献指南](#贡献指南)

---

## 01. 基础层

### 大语言模型

> **[待更新]** 商业模型名称/规格可能过时（OpenAI、Anthropic、Google、xAI 等）。开源部分已于 2025-05-24 通过 GitHub 验证。使用前请重新确认商业提供商的模型页面。

#### 商业 / 云端提供商

- **OpenAI**
  - [o3 / o3-mini](https://platform.openai.com/docs/models) - 下一代推理模型。
  - [o4-mini](https://platform.openai.com/docs/models) - 高性价比推理模型。
  - [GPT-4.1](https://platform.openai.com/docs/models) - 最新旗舰模型，指令遵循能力增强。
  - [GPT-4o](https://platform.openai.com/docs/models) - 多模态模型（文本、视觉、音频）。
  - [o1 / o1-mini](https://platform.openai.com/docs/models) - 思维链推理模型系列。

- **Anthropic**
  - [Claude Opus 4](https://docs.anthropic.com/en/docs/about-claude/models) - 最高能力模型，适合复杂多步骤任务。
  - [Claude Sonnet 4](https://docs.anthropic.com/en/docs/about-claude/models) - 旗舰混合推理模型，兼顾速度与深度。
  - [Claude 3.7 Sonnet](https://docs.anthropic.com/en/docs/about-claude/models) - 支持扩展思维的混合推理模型。
  - [Claude 3.5 Haiku](https://docs.anthropic.com/en/docs/about-claude/models) - 快速、高性价比模型。

- **Google DeepMind**
  - [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini) - 旗舰思维模型，100万+ token 上下文。
  - [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini) - 快速高性价比思维模型。
  - [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini) - 下一代多模态，原生工具调用。
  - [Gemma 3 / 3n](https://ai.google.dev/gemma) - 开源轻量模型，适合边缘部署。
  - [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini) - 长上下文模型，支持高达 200万 token。

- **Mistral AI**
  - [Mistral Large 2](https://docs.mistral.ai/getting-started/models/models_overview/) - 旗舰商业模型，多语言和编码能力突出。
  - [Mistral Medium 3](https://docs.mistral.ai/getting-started/models/models_overview/) - 高性能企业优化模型。
  - [Codestral](https://docs.mistral.ai/getting-started/models/models_overview/) - 专业代码生成模型。
  - [Mistral Small 3.1](https://docs.mistral.ai/getting-started/models/models_overview/) - 高效开源模型，支持视觉。
  - [Pixtral Large](https://docs.mistral.ai/getting-started/models/models_overview/) - 原生图像理解的多模态模型。

- **Cohere**
  - [Command A](https://docs.cohere.com/docs/models) - 旗舰 RAG 优化模型，支持智能体能力。
  - [Command R+](https://docs.cohere.com/docs/models) - 高性能 RAG 模型。
  - [Command R](https://docs.cohere.com/docs/models) - 生产级高效 RAG 模型。
  - [Embed v4](https://docs.cohere.com/docs/models) - 多模态嵌入模型。
  - [Rerank v3](https://docs.cohere.com/docs/models) - 搜索质量优化重排序模型。

- **Amazon（Bedrock & Titan）**
  - [Nova Pro](https://aws.amazon.com/bedrock/nova/) - 高能力多模态模型。
  - [Nova Lite](https://aws.amazon.com/bedrock/nova/) - 高吞吐量场景的高性价比模型。
  - [Nova Micro](https://aws.amazon.com/bedrock/nova/) - 最低延迟的纯文本模型。
  - [Titan Text Premier](https://aws.amazon.com/bedrock/) - 企业级文本生成模型。
  - [Nova Canvas](https://aws.amazon.com/bedrock/nova/) - 图像生成模型。

- **xAI**
  - [Grok 3](https://x.ai/docs) - 旗舰推理模型，深度搜索和编码。
  - [Grok 3 Mini](https://x.ai/docs) - 轻量推理模型。
  - [Grok 2](https://x.ai/docs) - 上一代多模态模型。
  - [Grok-1](https://x.ai/blog) - 开源 314B MoE 模型。
  - [Aurora](https://x.ai/docs) - 图像生成模型。

- **AI21 Labs**
  - [Jamba 1.5](https://docs.ai21.com/docs/jamba-models) - SSM-Transformer 混合架构，256K 上下文。
  - [Jamba 1.5 Mini](https://docs.ai21.com/docs/jamba-models) - 更小的 SSM-Transformer 混合模型。
  - [Jurassic-2 Ultra](https://docs.ai21.com/docs/j2-models) - 大规模企业级模型。
  - [Jurassic-2 Mid](https://docs.ai21.com/docs/j2-models) - 性能与成本平衡模型。

- **Reka**
  - [Reka Core](https://reka.ai/) - 旗舰多模态，视觉推理突出。
  - [Reka Flash](https://reka.ai/) - 快速多模态模型。
  - [Reka Edge](https://reka.ai/) - 轻量多模态边缘部署模型。

- **Writer**
  - [Palmyra X 004](https://writer.com/models/) - 高性能模型，工具调用能力强。
  - [Palmyra X 003](https://writer.com/models/) - 企业内容生成模型。

- **Perplexity**
  - [Sonar Pro](https://docs.perplexity.ai/) - 推理导向的搜索增强模型。
  - [Sonar](https://docs.perplexity.ai/) - 快速搜索增强生成模型。
  - [Sonar Reasoning](https://docs.perplexity.ai/) - 深度推理结合搜索。

- **Inflection AI**
  - [Inflection 3.0](https://inflection.ai/) - 企业级对话 AI 模型。
  - [Inflection 2.5](https://inflection.ai/) - 驱动 Pi 助手的高能力模型。

#### 开源 / 开放权重提供商

- **Meta**
  - [Llama 4 Maverick](https://llama.meta.com/) - 400B MoE 开源多模态模型（17B-128E）。
  - [Llama 4 Scout](https://llama.meta.com/) - 109B MoE 模型，1000万 token 上下文（17B-16E）。
  - [Llama 3.1 405B](https://llama.meta.com/) - 最大稠密开源模型。
  - [Llama 3.3 70B](https://llama.meta.com/) - 改进的 70B 参数模型。
  - [Llama 3.2 Vision](https://llama.meta.com/) - 开源多模态模型（11B/90B）。

- **DeepSeek**
  - [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) - 开源推理模型，对标 o1（671B MoE, 37B 激活）。
  - [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) - 开源 MoE，综合能力突出（671B, 37B 激活）。
  - [DeepSeek-Prover-V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2) - 定理证明专业模型。
  - [DeepSeek-R1-Distill](https://github.com/deepseek-ai/DeepSeek-R1) - 蒸馏推理模型（1.5B-70B，基于 Qwen & Llama）。
  - [Janus-Pro](https://github.com/deepseek-ai/DeepSeek-VL2) - 多模态理解与生成模型。

- **Qwen Team（阿里开源）**
  - [Qwen3-2507 (235B-A22B)](https://github.com/QwenLM/Qwen3) - 旗舰 MoE，混合思维，100万 token 上下文。
  - [Qwen3-2507 (30B-A3B)](https://github.com/QwenLM/Qwen3) - 高效 MoE 模型，经济部署。
  - [QwQ-32B](https://qwen.readthedocs.io/) - 开源推理模型。
  - [Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) - 基于 Qwen3 的代码专业模型。
  - [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) - 多模态视觉语言模型。

- **Microsoft**
  - [Phi-4](https://azure.microsoft.com/en-us/products/phi) - 14B 模型，超越量级表现。
  - [Phi-4-reasoning](https://github.com/microsoft/Phi-4-reasoning-vision-15B) - 15B 推理模型，支持视觉。
  - [Phi-4-mini](https://azure.microsoft.com/en-us/products/phi) - 紧凑 3.8B 模型，适合边缘/移动端。
  - [Phi-3.5 MoE](https://azure.microsoft.com/en-us/products/phi) - 混合专家高效模型。
  - [Phi-3 Vision](https://azure.microsoft.com/en-us/products/phi) - 轻量多模态模型。

- **NVIDIA**
  - [Nemotron-Ultra 253B](https://build.nvidia.com/) - 微调推理模型。
  - [Nemotron-4 340B](https://build.nvidia.com/) - 大型开源合成数据模型。
  - [NVLM](https://build.nvidia.com/) - 开源多模态大语言模型。
  - [Nemotron-H](https://build.nvidia.com/) - 高效边缘部署模型系列。

- **Databricks**
  - [DBRX Instruct](https://www.databricks.com/) - 开源 132B MoE 指令遵循模型。
  - [DBRX Base](https://www.databricks.com/) - 开源基础 MoE 模型。

- **Snowflake**
  - [Arctic](https://docs.snowflake.com/) - 开源 480B MoE 企业任务模型。
  - [Arctic Embed](https://docs.snowflake.com/) - 高质量开源嵌入模型。

- **Allen AI（AI2）**
  - [OLMo 2](https://allenai.org/) - 完全开源 LLM，含训练数据和代码。
  - [Tulu 3](https://allenai.org/) - 开源后训练模型系列。
  - [OLMoE](https://allenai.org/) - 开源混合专家模型。

- **Stability AI**
  - [StableLM 2 12B](https://stability.ai/) - 开源语言模型。
  - [Stable Code Instruct 3B](https://stability.ai/) - 紧凑开源代码模型。

- **Hugging Face（社区）**
  - [Zephyr](https://huggingface.co/HuggingFaceH4) - 基于 Mistral 的微调对话模型。
  - [SmolLM2](https://huggingface.co/HuggingFaceTB) - 紧凑端侧模型（135M-1.7B）。
  - [Tulu 3](https://huggingface.co/allenai) - 开源后训练方案和模型。

- **Cohere For AI（研究）**
  - [Aya 23](https://cohere.com/research) - 开源多语言模型（23种语言）。
  - [Aya Expanse](https://cohere.com/research) - 业界领先多语言模型。
  - [Command R7B](https://cohere.com/research) - 紧凑开源 RAG 模型。

#### 中国生态

- **阿里云（通义千问）**
  - [Qwen-Max](https://tongyi.aliyun.com/) - 旗舰商业 API，推理能力突出。
  - [Qwen-Plus](https://tongyi.aliyun.com/) - 性能与成本均衡。
  - [Qwen-Turbo](https://tongyi.aliyun.com/) - 超快速模型，适合高吞吐场景。
  - [Qwen-VL-Max](https://tongyi.aliyun.com/) - 商业多模态视觉语言模型。
  - [Qwen-Long](https://tongyi.aliyun.com/) - 长上下文文档处理模型。

- **百度（文心一言 / ERNIE）**
  - [ERNIE 4.5](https://yiyan.baidu.com/) - 下一代模型，推理能力提升。
  - [ERNIE 4.0](https://yiyan.baidu.com/) - 旗舰模型，中文理解力突出。
  - [ERNIE 3.5](https://yiyan.baidu.com/) - 高性价比生产模型。
  - [ERNIE Speed / Lite](https://yiyan.baidu.com/) - 快速推理，适合高并发场景。
  - [ERNIE Functions](https://yiyan.baidu.com/) - 工具调用优化模型。

- **智谱 AI（智谱清言）**
  - [GLM-4-Plus](https://bigmodel.cn/) - 旗舰通用模型。
  - [GLM-4V-Plus](https://bigmodel.cn/) - 多模态视觉语言模型。
  - [GLM-4-Long](https://bigmodel.cn/) - 长上下文模型（128K+ token）。
  - [GLM-4-Flash](https://bigmodel.cn/) - 免费快速推理模型。
  - [CogVideoX](https://bigmodel.cn/) - 开源视频生成模型。

- **月之暗面（Kimi）**
  - [Kimi k2](https://kimi.moonshot.cn/) - 旗舰模型，长上下文能力突出（200K token）。
  - [Moonshot-v1](https://platform.moonshot.cn/) - API 模型系列（8K/32K/128K 上下文）。

- **字节跳动（豆包 / Doubao / Seed）**
  - [Seed1.5-VL](https://github.com/ByteDance-Seed/Seed1.5-VL) - 旗舰视觉语言 MoE 模型（20B 激活参数）。
  - [Doubao-Pro](https://team.doubao.com/) - 旗舰商业模型。
  - [Doubao-Lite](https://team.doubao.com/) - 轻量快速模型。
  - [Doubao-Embedding](https://team.doubao.com/) - 文本嵌入模型。

- **腾讯（混元 / Hunyuan）**
  - [Hunyuan TurboS](https://github.com/Tencent/Hunyuan-TurboS) - 旗舰快思考 MoE 模型，Hybrid-Mamba-Transformer 架构。
  - [Hunyuan T1](https://github.com/Tencent/llm.hunyuan.T1) - 强化学习驱动的推理模型。
  - [Hunyuan-Large](https://hunyuan.tencent.com/) - 开源 389B MoE 模型。
  - [Hunyuan-Pro](https://hunyuan.tencent.com/) - 商业 API 旗舰模型。
  - [Hunyuan-Video](https://hunyuan.tencent.com/) - 开源视频生成模型。

- **MiniMax（海螺AI）**
  - [MiniMax-Text-01](https://www.minimaxi.com/) - 开源 456B MoE 长上下文模型。
  - [abab 7](https://www.minimaxi.com/) - 商业对话/补全模型。
  - [abab 6.5s](https://www.minimaxi.com/) - 高性价比生产模型。
  - [Video-01](https://www.minimaxi.com/) - 视频生成模型。
  - [Speech-01](https://www.minimaxi.com/) - 文本转语音模型。

- **百川智能**
  - [Baichuan 4](https://www.baichuan-ai.com/) - 旗舰模型，推理和编码能力突出。
  - [Baichuan 3](https://www.baichuan-ai.com/) - 上一代通用模型。
  - [Baichuan 2 (13B)](https://www.baichuan-ai.com/) - 开源双语模型。

- **零一万物**
  - [Yi-Lightning](https://www.01.ai/) - 超快速高性价比模型。
  - [Yi Vision](https://www.01.ai/) - 多模态视觉语言模型。
  - [Yi-34B / Yi-9B](https://www.01.ai/) - 开源双语模型。

- **科大讯飞（讯飞星火）**
  - [Spark 4.0 Ultra](https://xinghuo.xfyun.cn/) - 旗舰模型，中文教育能力突出。
  - [Spark 4.0](https://xinghuo.xfyun.cn/) - 通用企业模型。
  - [Spark 3.5 Max](https://xinghuo.xfyun.cn/) - 高性价比生产模型。

- **商汤（日日新 / SenseNova）**
  - [SenseNova 5.5](https://sensenova.sensetime.com/) - 旗舰多模态模型。
  - [SenseNova 5.0](https://sensenova.sensetime.com/) - 上一代高能力模型。

#### 端侧 / 边缘

- **Apple** - [AFM（Apple Foundation Model）](https://machinelearning.apple.com/) - 端侧和服务端模型，驱动 Apple Intelligence。
- **Samsung** - [Samsung Gauss](https://research.samsung.com/) - Galaxy 生态的端侧和服务端 LLM。

#### 推理平台（托管开源模型）

- [Together AI](https://together.ai/) - 200+ 开源模型的无服务器推理。
- [Fireworks AI](https://fireworks.ai/) - 快速高性价比开源 LLM 服务。
- [Groq](https://groq.com/) - 基于 LPU 的超快推理。
- [Cerebras](https://cerebras.ai/) - 晶圆级推理加速。

### 提示工程

<details>
<summary><b>系统提示</b> — LLM 系统提示合集与工具</summary>

- [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) ![Stars](https://img.shields.io/github/stars/x1xhlol/system-prompts-and-models-of-ai-tools?style=social) - 从 Augment Code、Claude Code、Cursor、Devin、Manus、Perplexity、Windsurf、v0 等提取的完整系统提示。
- [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) ![Stars](https://img.shields.io/github/stars/asgeirtj/system_prompts_leaks?style=social) - ChatGPT、Claude、Gemini、Grok、Copilot、Perplexity 等系统提示提取。
- [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) ![Stars](https://img.shields.io/github/stars/elder-plinius/CL4R1T4S?style=social) - 泄露的系统提示合集——ChatGPT、Claude、Gemini、Grok、Cursor、Lovable、Replit。
- [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) ![Stars](https://img.shields.io/github/stars/jujumilk3/leaked-system-prompts?style=social) - 各类 LLM 产品泄露系统提示收集。
- [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt) ![Stars](https://img.shields.io/github/stars/LouisShark/chatgpt_system_prompt?style=social) - GPT 系统提示收集，含提示注入和泄露技术。
- [claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) ![Stars](https://img.shields.io/github/stars/Piebald-AI/claude-code-system-prompts?style=social) - Claude Code 完整系统提示：27 个内置工具、子代理提示、工具提示。
- [awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) ![Stars](https://img.shields.io/github/stars/dontriskit/awesome-ai-system-prompts?style=social) - 精选系统提示——ChatGPT、Claude、Perplexity、Manus、Claude Code、Lovable、v0、Grok。
- [TheBigPromptLibrary](https://github.com/0xeb/TheBigPromptLibrary) ![Stars](https://img.shields.io/github/stars/0xeb/TheBigPromptLibrary?style=social) - 大型提示、系统提示和 LLM 指令合集。
- [tweakcc](https://github.com/Piebald-AI/tweakcc) ![Stars](https://img.shields.io/github/stars/Piebald-AI/tweakcc?style=social) - 自定义 Claude Code 系统提示、工具集和主题。
- [awesome-system-prompts](https://github.com/langgptai/awesome-system-prompts) ![Stars](https://img.shields.io/github/stars/langgptai/awesome-system-prompts?style=social) - DeepSeek、ChatGPT、Gemini、Grok、Qwen 的系统提示。

</details>

<details>
<summary><b>少样本 / 上下文学习</b> — 从示范中学习</summary>

- [Otter](https://github.com/EvolvingLMMs-Lab/Otter) ![Stars](https://img.shields.io/github/stars/EvolvingLMMs-Lab/Otter?style=social) - 多模态模型，指令遵循和上下文学习能力提升。
- [prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning) ![Stars](https://img.shields.io/github/stars/EgoAlpha/prompt-in-context-learning?style=social) - 上下文学习和提示工程精选资源。
- [ICL_PaperList](https://github.com/dqxiu/ICL_PaperList) ![Stars](https://img.shields.io/github/stars/dqxiu/ICL_PaperList?style=social) - 上下文学习研究论文精选。
- [OpenICL](https://github.com/Shark-NLP/OpenICL) ![Stars](https://img.shields.io/github/stars/Shark-NLP/OpenICL?style=social) - 上下文学习研究与原型开发开源框架。
- [DINOv](https://github.com/UX-Decoder/DINOv) ![Stars](https://img.shields.io/github/stars/UX-Decoder/DINOv?style=social) - 视觉上下文学习（CVPR 2024）。
- [t-few](https://github.com/r-three/t-few) ![Stars](https://img.shields.io/github/stars/r-three/t-few?style=social) - 少样本参数高效微调 vs 上下文学习对比。
- [xmc.dspy](https://github.com/KarelDO/xmc.dspy) ![Stars](https://img.shields.io/github/stars/KarelDO/xmc.dspy?style=social) - 极端多标签分类的上下文学习。
- [prompt-lib](https://github.com/reasoning-machines/prompt-lib) ![Stars](https://img.shields.io/github/stars/reasoning-machines/prompt-lib?style=social) - LLM 少样本提示实验工具。
- [TextualExplInContext](https://github.com/xiye17/TextualExplInContext) ![Stars](https://img.shields.io/github/stars/xiye17/TextualExplInContext?style=social) - 少样本提示中解释的不可靠性（NeurIPS 2022）。
- [bullet](https://github.com/rafaelpierre/bullet) ![Stars](https://img.shields.io/github/stars/rafaelpierre/bullet?style=social) - 零样本/少样本 LLM 文本分类框架。

</details>

<details>
<summary><b>思维链 / 推理</b> — 逐步推理技术</summary>

- [Awesome-LLM-Strawberry](https://github.com/hijkzzz/Awesome-LLM-Strawberry) ![Stars](https://img.shields.io/github/stars/hijkzzz/Awesome-LLM-Strawberry?style=social) - OpenAI o1 及推理技术论文和项目合集。
- [tree-of-thought-llm](https://github.com/princeton-nlp/tree-of-thought-llm) ![Stars](https://img.shields.io/github/stars/princeton-nlp/tree-of-thought-llm?style=social) - 思维树：LLM 深思问题求解（NeurIPS 2023）。
- [deepreasoning](https://github.com/winfunc/deepreasoning) ![Stars](https://img.shields.io/github/stars/winfunc/deepreasoning?style=social) - DeepSeek R1 CoT 推理轨迹与 Claude 模型集成。
- [tree-of-thoughts](https://github.com/kyegomez/tree-of-thoughts) ![Stars](https://img.shields.io/github/stars/kyegomez/tree-of-thoughts?style=social) - 即插即用思维树实现。
- [reasoning-from-scratch](https://github.com/rasbt/reasoning-from-scratch) ![Stars](https://img.shields.io/github/stars/rasbt/reasoning-from-scratch?style=social) - 从零开始用 PyTorch 实现推理 LLM。
- [mm-cot](https://github.com/amazon-science/mm-cot) ![Stars](https://img.shields.io/github/stars/amazon-science/mm-cot?style=social) - 多模态思维链推理。
- [Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) ![Stars](https://img.shields.io/github/stars/atfortes/Awesome-LLM-Reasoning?style=social) - 从 CoT 到 o1 和 DeepSeek-R1 的推理资源列表。
- [chain-of-thought-hub](https://github.com/FranxYao/chain-of-thought-hub) ![Stars](https://img.shields.io/github/stars/FranxYao/chain-of-thought-hub?style=social) - CoT 提示下 LLM 复杂推理能力基准测试。
- [Chain-of-ThoughtsPapers](https://github.com/Timothyxxx/Chain-of-ThoughtsPapers) ![Stars](https://img.shields.io/github/stars/Timothyxxx/Chain-of-ThoughtsPapers?style=social) - CoT 推理趋势论文集。
- [auto-cot](https://github.com/amazon-science/auto-cot) ![Stars](https://img.shields.io/github/stars/amazon-science/auto-cot?style=social) - LLM 自动思维链提示。

</details>

<details>
<summary><b>结构化输出</b> — JSON、模式与约束生成</summary>

- [guidance](https://github.com/guidance-ai/guidance) ![Stars](https://img.shields.io/github/stars/guidance-ai/guidance?style=social) - 基于约束的模板生成，控制 LLM 输出。
- [pydantic-ai](https://github.com/pydantic/pydantic-ai) ![Stars](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=social) - AI 代理框架——通过 Pydantic 类型注解实现结构化输出。
- [outlines](https://github.com/dottxt-ai/outlines) ![Stars](https://img.shields.io/github/stars/dottxt-ai/outlines?style=social) - 基于 token 级约束解码的结构化生成（regex、JSON Schema、CFG）。
- [instructor](https://github.com/567-labs/instructor) ![Stars](https://img.shields.io/github/stars/567-labs/instructor?style=social) - 为 OpenAI/Anthropic 客户端打补丁，返回 Pydantic 模型。
- [TypeChat](https://github.com/microsoft/TypeChat) ![Stars](https://img.shields.io/github/stars/microsoft/TypeChat?style=social) - 使用 TypeScript 类型将自然语言意图映射为类型化 JSON。
- [guardrails](https://github.com/guardrails-ai/guardrails) ![Stars](https://img.shields.io/github/stars/guardrails-ai/guardrails?style=social) - LLM 输入/输出验证、模式执行和重新询问。
- [jsonformer](https://github.com/1rgs/jsonformer) ![Stars](https://img.shields.io/github/stars/1rgs/jsonformer?style=social) - 通过约束解码实现可靠的结构化 JSON 生成。
- [lmql](https://github.com/eth-sri/lmql) ![Stars](https://img.shields.io/github/stars/eth-sri/lmql?style=social) - 声明式约束语言，用于引导 LLM 编程。
- [lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer) ![Stars](https://img.shields.io/github/stars/noamgat/lm-format-enforcer?style=social) - 在生成时强制执行 JSON Schema、Regex 等格式。
- [xgrammar](https://github.com/mlc-ai/xgrammar) ![Stars](https://img.shields.io/github/stars/mlc-ai/xgrammar?style=social) - 快速基于语法的约束解码结构化生成。

</details>

### 上下文

<details>
<summary><b>记忆</b> — AI 代理的长期和短期记忆</summary>

- [mempalace](https://github.com/MemPalace/mempalace) ![Stars](https://img.shields.io/github/stars/MemPalace/mempalace?style=social) - 基准测试最优的开源 AI 记忆系统。
- [mem0](https://github.com/mem0ai/mem0) ![Stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social) - AI 代理记忆层。
- [letta](https://github.com/letta-ai/letta) ![Stars](https://img.shields.io/github/stars/letta-ai/letta?style=social) - 基于 MemGPT 构建有状态 LLM 代理。
- [hindsight](https://github.com/vectorize-io/hindsight) ![Stars](https://img.shields.io/github/stars/vectorize-io/hindsight?style=social) - 能学习的代理记忆。
- [TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) ![Stars](https://img.shields.io/github/stars/Tencent/TencentDB-Agent-Memory?style=social) - 全本地四级渐进式记忆管线，零外部 API 依赖。
- [A-MEM](https://github.com/agiresearch/A-MEM) ![Stars](https://img.shields.io/github/stars/agiresearch/A-MEM?style=social) - LLM 代理的自主记忆系统。
- [Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory) ![Stars](https://img.shields.io/github/stars/IAAR-Shanghai/Awesome-AI-Memory?style=social) - AI 记忆精选知识库——研究、框架、基准测试。
- [general-agentic-memory](https://github.com/VectorSpaceLab/general-agentic-memory) ![Stars](https://img.shields.io/github/stars/VectorSpaceLab/general-agentic-memory?style=social) - 基于深度研究的通用代理记忆系统。
- [mcp-mem0](https://github.com/coleam00/mcp-mem0) ![Stars](https://img.shields.io/github/stars/coleam00/mcp-mem0?style=social) - 集成 Mem0 的长期代理记忆 MCP 服务器。
- [memoir](https://github.com/zhangfengcdt/memoir) ![Stars](https://img.shields.io/github/stars/zhangfengcdt/memoir?style=social) - 类 Git 版本控制的分层代理记忆。

</details>

<details>
<summary><b>RAG</b> — 检索增强生成框架与工具</summary>

- [ragflow](https://github.com/infiniflow/ragflow) ![Stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social) - 领先的开源 RAG 引擎，融合代理能力。
- [LightRAG](https://github.com/HKUDS/LightRAG) ![Stars](https://img.shields.io/github/stars/HKUDS/LightRAG?style=social) - 简单快速的检索增强生成（EMNLP 2025）。
- [graphrag](https://github.com/microsoft/graphrag) ![Stars](https://img.shields.io/github/stars/microsoft/graphrag?style=social) - 微软模块化图基 RAG 系统。
- [RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) ![Stars](https://img.shields.io/github/stars/NirDiamant/RAG_Techniques?style=social) - 高级 RAG 技术，含详细 notebook 教程。
- [memvid](https://github.com/memvid/memvid) ![Stars](https://img.shields.io/github/stars/memvid/memvid?style=social) - 无服务器单文件 RAG 管线替代方案。
- [llmware](https://github.com/llmware-ai/llmware) ![Stars](https://img.shields.io/github/stars/llmware-ai/llmware?style=social) - 基于小型专业模型的企业 RAG 统一框架。
- [orama](https://github.com/oramasearch/orama) ![Stars](https://img.shields.io/github/stars/oramasearch/orama?style=social) - 全文、向量和混合搜索的完整搜索引擎。
- [R2R](https://github.com/SciPhi-AI/R2R) ![Stars](https://img.shields.io/github/stars/SciPhi-AI/R2R?style=social) - 生产就绪的代理式 RAG，带 RESTful API。
- [Verba](https://github.com/weaviate/Verba) ![Stars](https://img.shields.io/github/stars/weaviate/Verba?style=social) - 基于 Weaviate 的 RAG 聊天机器人。
- [azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo) ![Stars](https://img.shields.io/github/stars/Azure-Samples/azure-search-openai-demo?style=social) - Azure AI Search + OpenAI 参考问答应用。

</details>

<details>
<summary><b>向量数据库</b> — 嵌入存储与搜索</summary>

- [milvus](https://github.com/milvus-io/milvus) ![Stars](https://img.shields.io/github/stars/milvus-io/milvus?style=social) - 高性能云原生向量数据库，支持 ANN 搜索。
- [faiss](https://github.com/facebookresearch/faiss) ![Stars](https://img.shields.io/github/stars/facebookresearch/faiss?style=social) - 高效稠密向量相似搜索与聚类库。
- [qdrant](https://github.com/qdrant/qdrant) ![Stars](https://img.shields.io/github/stars/qdrant/qdrant?style=social) - 高性能向量数据库和搜索引擎。
- [chroma](https://github.com/chroma-core/chroma) ![Stars](https://img.shields.io/github/stars/chroma-core/chroma?style=social) - 开源 AI 嵌入数据库。
- [pgvector](https://github.com/pgvector/pgvector) ![Stars](https://img.shields.io/github/stars/pgvector/pgvector?style=social) - PostgreSQL 向量相似搜索扩展。
- [weaviate](https://github.com/weaviate/weaviate) ![Stars](https://img.shields.io/github/stars/weaviate/weaviate?style=social) - 开源向量数据库，支持结构化过滤。
- [lancedb](https://github.com/lancedb/lancedb) ![Stars](https://img.shields.io/github/stars/lancedb/lancedb?style=social) - 开发者友好的多模态 AI 嵌入式检索库。
- [RediSearch](https://github.com/RediSearch/RediSearch) ![Stars](https://img.shields.io/github/stars/RediSearch/RediSearch?style=social) - Redis 查询与索引引擎，支持向量相似搜索。
- [helix-db](https://github.com/HelixDB/helix-db) ![Stars](https://img.shields.io/github/stars/HelixDB/helix-db?style=social) - Rust 实现的开源图向量数据库。
- [cozo](https://github.com/cozodb/cozo) ![Stars](https://img.shields.io/github/stars/cozodb/cozo?style=social) - 事务型关系-图-向量数据库，使用 Datalog 查询。

</details>

<details>
<summary><b>知识图谱</b> — AI 代理的结构化知识</summary>

- [graphify](https://github.com/safishamsi/graphify) ![Stars](https://img.shields.io/github/stars/safishamsi/graphify?style=social) - 将任意文件夹转为 AI 编码助手可查询的知识图谱。
- [GitNexus](https://github.com/abhigyanpatwari/GitNexus) ![Stars](https://img.shields.io/github/stars/abhigyanpatwari/GitNexus?style=social) - 零服务器客户端知识图谱，内置 Graph RAG 代理。
- [graphiti](https://github.com/getzep/graphiti) ![Stars](https://img.shields.io/github/stars/getzep/graphiti?style=social) - 为 AI 代理构建实时知识图谱。
- [Understand-Anything](https://github.com/Lum1104/Understand-Anything) ![Stars](https://img.shields.io/github/stars/Lum1104/Understand-Anything?style=social) - 将任意代码转为可交互、可搜索的知识图谱。
- [codegraph](https://github.com/colbymchenry/codegraph) ![Stars](https://img.shields.io/github/stars/colbymchenry/codegraph?style=social) - 为 Claude Code、Cursor、Codex 预索引的代码知识图谱。
- [code-review-graph](https://github.com/tirth8205/code-review-graph) ![Stars](https://img.shields.io/github/stars/tirth8205/code-review-graph?style=social) - Claude Code 本地代码知识图谱映射。
- [QASystemOnMedicalKG](https://github.com/liuhuanyong/QASystemOnMedicalKG) ![Stars](https://img.shields.io/github/stars/liuhuanyong/QASystemOnMedicalKG?style=social) - 医学知识图谱构建与问答系统。
- [KnowledgeGraphData](https://github.com/ownthink/KnowledgeGraphData) ![Stars](https://img.shields.io/github/stars/ownthink/KnowledgeGraphData?style=social) - 1.4 亿实体中文知识图谱开放数据集。
- [DeepKE](https://github.com/zjunlp/DeepKE) ![Stars](https://img.shields.io/github/stars/zjunlp/DeepKE?style=social) - 知识图谱抽取与构建工具包（EMNLP 2022）。
- [Yuxi](https://github.com/xerrors/Yuxi) ![Stars](https://img.shields.io/github/stars/xerrors/Yuxi?style=social) - 集成 LightRAG + 知识图谱 + MCP 的多租户代理平台。

</details>

---

## 02. 代理大脑

### 规划

<details>
<summary><b>任务分解</b> — 将目标拆分为子任务</summary>

- [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) ![Stars](https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=social) - 层级多代理系统，自动任务分解。
- [Plan-and-Solve-Prompting](https://github.com/AGI-Edgerunners/Plan-and-Solve-Prompting) ![Stars](https://img.shields.io/github/stars/AGI-Edgerunners/Plan-and-Solve-Prompting?style=social) - 计划-求解提示法（ACL 2023）。
- [babyagi](https://github.com/yoheinakajima/babyagi) ![Stars](https://img.shields.io/github/stars/yoheinakajima/babyagi?style=social) - 任务分解与优先级排序代理。
- [full-self-coding](https://github.com/NO-CHATBOT-REVOLUTION/full-self-coding) ![Stars](https://img.shields.io/github/stars/NO-CHATBOT-REVOLUTION/full-self-coding?style=social) - 100-1000 个 AI 代理并行编码，自主任务分解。
- [lemon-agent](https://github.com/felixbrock/lemon-agent) ![Stars](https://img.shields.io/github/stars/felixbrock/lemon-agent?style=social) - 计划-验证-求解代理，工作流自动化。
- [ANWS](https://github.com/Haaaiawd/ANWS) ![Stars](https://img.shields.io/github/stars/Haaaiawd/ANWS?style=social) - PRD→架构→任务分解框架。
- [langchain-huggingGPT](https://github.com/camille-vanhoffelen/langchain-huggingGPT) ![Stars](https://img.shields.io/github/stars/camille-vanhoffelen/langchain-huggingGPT?style=social) - Langchain 版 HuggingGPT，子任务规划。
- [pi-squad](https://github.com/picassio/pi-squad) ![Stars](https://img.shields.io/github/stars/picassio/pi-squad?style=social) - 多代理协作，任务分解与并行执行。
- [SagaLLM](https://github.com/genglongling/SagaLLM) ![Stars](https://img.shields.io/github/stars/genglongling/SagaLLM?style=social) - 多代理规划的上下文管理与事务保障。
- [HEIM](https://github.com/merocle/HEIM) ![Stars](https://img.shields.io/github/stars/merocle/HEIM?style=social) - 混合企业推理网格，任务分解与路由。

</details>

<details>
<summary><b>目标路由</b> — 语义路由与意图分类</summary>

- [plano](https://github.com/katanemo/plano) ![Stars](https://img.shields.io/github/stars/katanemo/plano?style=social) - AI 原生代理，智能 LLM 路由与编排。
- [RouteLLM](https://github.com/lm-sys/RouteLLM) ![Stars](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=social) - LLM 路由服务与评估框架。
- [semantic-router](https://github.com/aurelio-labs/semantic-router) ![Stars](https://img.shields.io/github/stars/aurelio-labs/semantic-router?style=social) - 超快 AI 决策与语义路由。
- [semantic-router (vllm)](https://github.com/vllm-project/semantic-router) ![Stars](https://img.shields.io/github/stars/vllm-project/semantic-router?style=social) - 混合模型系统级智能路由。
- [LLMRouter](https://github.com/ulab-uiuc/LLMRouter) ![Stars](https://img.shields.io/github/stars/ulab-uiuc/LLMRouter?style=social) - LLM 路由开源库。
- [WilmerAI](https://github.com/SomeOddCodeGuy/WilmerAI) ![Stars](https://img.shields.io/github/stars/SomeOddCodeGuy/WilmerAI?style=social) - LLM 应用多层提示路由。
- [OrcaRouter-Lite](https://github.com/Continuum-AI-Corp/OrcaRouter-Lite) ![Stars](https://img.shields.io/github/stars/Continuum-AI-Corp/OrcaRouter-Lite?style=social) - 自托管 LLM 路由，带安全兜底。
- [UncommonRoute](https://github.com/CommonstackAI/UncommonRoute) ![Stars](https://img.shields.io/github/stars/CommonstackAI/UncommonRoute?style=social) - 自动 LLM 路由，节省 82% 成本。

</details>

<details>
<summary><b>反思</b> — 自我精炼与语言强化学习</summary>

- [reflexion](https://github.com/noahshinn/reflexion) ![Stars](https://img.shields.io/github/stars/noahshinn/reflexion?style=social) - Reflexion：语言代理的语言强化学习（NeurIPS 2023）。
- [self-rag](https://github.com/AkariAsai/self-rag) ![Stars](https://img.shields.io/github/stars/AkariAsai/self-rag?style=social) - SELF-RAG：通过自我反思学习检索、生成和批评。
- [self-refine](https://github.com/madaan/self-refine) ![Stars](https://img.shields.io/github/stars/madaan/self-refine?style=social) - LLM 生成反馈并迭代改进输出。
- [langgraph-course](https://github.com/emarco177/langgraph-course) ![Stars](https://img.shields.io/github/stars/emarco177/langgraph-course?style=social) - LangGraph 课程，含反思工作流模式。
- [self-correction-llm-papers](https://github.com/teacherpeterpan/self-correction-llm-papers) ![Stars](https://img.shields.io/github/stars/teacherpeterpan/self-correction-llm-papers?style=social) - 自纠错 LLM 研究论文合集。
- [self-reflection](https://github.com/matthewrenze/self-reflection) ![Stars](https://img.shields.io/github/stars/matthewrenze/self-reflection?style=social) - 自我反思对问题求解性能的影响。
- [SuperCorrect-llm](https://github.com/YangLing0818/SuperCorrect-llm) ![Stars](https://img.shields.io/github/stars/YangLing0818/SuperCorrect-llm?style=social) - 思维模板蒸馏与自我纠错（ICLR 2025）。
- [llm-self-correction-papers](https://github.com/ryokamoi/llm-self-correction-papers) ![Stars](https://img.shields.io/github/stars/ryokamoi/llm-self-correction-papers?style=social) - LLM 自纠错论文精选列表。

</details>

### 推理

<details>
<summary><b>ReAct</b> — 推理与行动协同</summary>

- [ReAct](https://github.com/ysymyth/ReAct) ![Stars](https://img.shields.io/github/stars/ysymyth/ReAct?style=social) - ReAct 官方实现（ICLR 2023）。
- [react-agent](https://github.com/eylonmiz/react-agent) ![Stars](https://img.shields.io/github/stars/eylonmiz/react-agent?style=social) - 开源自主 LLM 代理，实现 ReAct 模式。
- [react-agent (LangGraph)](https://github.com/langchain-ai/react-agent) ![Stars](https://img.shields.io/github/stars/langchain-ai/react-agent?style=social) - LangGraph ReAct 代理模板。
- [langgraph-mcp-agents](https://github.com/braincrew-lab/langgraph-mcp-agents) ![Stars](https://img.shields.io/github/stars/braincrew-lab/langgraph-mcp-agents?style=social) - 集成 MCP 的 ReAct 代理。
- [CookHero](https://github.com/Decade-qiu/CookHero) ![Stars](https://img.shields.io/github/stars/Decade-qiu/CookHero?style=social) - LLM + RAG + ReAct 智能烹饪平台。
- [quantalogic](https://github.com/quantalogic/quantalogic) ![Stars](https://img.shields.io/github/stars/quantalogic/quantalogic?style=social) - 基于 ReAct 的编码代理框架。
- [LangChain-ReAct-Agent](https://github.com/lhh737/LangChain-ReAct-Agent) ![Stars](https://img.shields.io/github/stars/lhh737/LangChain-ReAct-Agent?style=social) - LangChain/Graph ReAct 代理，RAG + 工具调用。
- [llm-ReAct](https://github.com/OceanPresentChao/llm-ReAct) ![Stars](https://img.shields.io/github/stars/OceanPresentChao/llm-ReAct?style=social) - 从零构建 LLM ReAct 代理（教程）。

</details>

<details>
<summary><b>思维树</b> — 通过树搜索进行审慎推理</summary>

- [tree-of-thought-llm](https://github.com/princeton-nlp/tree-of-thought-llm) ![Stars](https://img.shields.io/github/stars/princeton-nlp/tree-of-thought-llm?style=social) - 思维树（NeurIPS 2023）。
- [tree-of-thoughts](https://github.com/kyegomez/tree-of-thoughts) ![Stars](https://img.shields.io/github/stars/kyegomez/tree-of-thoughts?style=social) - 即插即用思维树实现。
- [graph-of-thoughts](https://github.com/spcl/graph-of-thoughts) ![Stars](https://img.shields.io/github/stars/spcl/graph-of-thoughts?style=social) - 思维图（ETH Zurich）。
- [Neurite](https://github.com/satellitecomponent/Neurite) ![Stars](https://img.shields.io/github/stars/satellitecomponent/Neurite?style=social) - 分形思维图 AI 代理思维导图。
- [tree-of-thought-prompting](https://github.com/dave1010/tree-of-thought-prompting) ![Stars](https://img.shields.io/github/stars/dave1010/tree-of-thought-prompting?style=social) - 思维树提示提升推理能力。
- [MindMap](https://github.com/wyl-willing/MindMap) ![Stars](https://img.shields.io/github/stars/wyl-willing/MindMap?style=social) - 知识图谱提示激发思维图。
- [tree-of-thought-puzzle-solver](https://github.com/jieyilong/tree-of-thought-puzzle-solver) ![Stars](https://img.shields.io/github/stars/jieyilong/tree-of-thought-puzzle-solver?style=social) - 思维树框架解决复杂推理任务。
- [knowledge-graph-of-thoughts](https://github.com/spcl/knowledge-graph-of-thoughts) ![Stars](https://img.shields.io/github/stars/spcl/knowledge-graph-of-thoughts?style=social) - 知识图谱思维实现经济型 AI 助手。

</details>

<details>
<summary><b>多代理辩论</b> — 通过辩论进行协作推理</summary>

- [Multi-Agents-Debate](https://github.com/Skytliang/Multi-Agents-Debate) ![Stars](https://img.shields.io/github/stars/Skytliang/Multi-Agents-Debate?style=social) - MAD：LLM 多代理辩论。
- [ChatEval](https://github.com/thunlp/ChatEval) ![Stars](https://img.shields.io/github/stars/thunlp/ChatEval?style=social) - 通过多代理辩论提升 LLM 评估。
- [llm_debate](https://github.com/ucl-dark/llm_debate) ![Stars](https://img.shields.io/github/stars/ucl-dark/llm_debate?style=social) - 与更有说服力的 LLM 辩论（UCL DARK）。
- [magi](https://github.com/fshiori/magi) ![Stars](https://img.shields.io/github/stars/fshiori/magi?style=social) - 三个 LLM 辩论做出更好决策。
- [Agent-Debate](https://github.com/starshine-f/Agent-Debate) ![Stars](https://img.shields.io/github/stars/starshine-f/Agent-Debate?style=social) - AI vs AI 和人类 vs AI 多代理辩论。
- [DebateLLM](https://github.com/instadeepai/DebateLLM) ![Stars](https://img.shields.io/github/stars/instadeepai/DebateLLM?style=social) - 多代理辩论真实性基准。
- [SWE-Debate](https://github.com/YerbaPage/SWE-Debate) ![Stars](https://img.shields.io/github/stars/YerbaPage/SWE-Debate?style=social) - 软件问题解决的竞争性辩论（ICSE 2026）。
- [M-MAD](https://github.com/SU-JIAYUAN/M-MAD) ![Stars](https://img.shields.io/github/stars/SU-JIAYUAN/M-MAD?style=social) - 多维辩论翻译评估（ACL 2025）。

</details>

<details>
<summary><b>自我修正</b> — 迭代修复与调试</summary>

- [SWE-agent](https://github.com/SWE-agent/SWE-agent) ![Stars](https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=social) - 自动修复 GitHub Issue 的自主代理（NeurIPS 2024）。
- [AlphaCodium](https://github.com/Codium-ai/AlphaCodium) ![Stars](https://img.shields.io/github/stars/Codium-ai/AlphaCodium?style=social) - 代码生成的迭代自我纠错。
- [automata](https://github.com/emrgnt-cmplxty/automata) ![Stars](https://img.shields.io/github/stars/emrgnt-cmplxty/automata?style=social) - 自编码代理，编写、执行并自我纠错。
- [MapCoder](https://github.com/Md-Ashraful-Pramanik/MapCoder) ![Stars](https://img.shields.io/github/stars/Md-Ashraful-Pramanik/MapCoder?style=social) - 含自我调试的多代理代码生成。
- [STELLA](https://github.com/zaixizhang/STELLA) ![Stars](https://img.shields.io/github/stars/zaixizhang/STELLA?style=social) - 生物医学研究的自进化 LLM 代理。
- [DiagGym](https://github.com/MAGIC-AI4Med/DiagGym) ![Stars](https://img.shields.io/github/stars/MAGIC-AI4Med/DiagGym?style=social) - 自进化诊断代理的虚拟临床环境。
- [RepairAgent](https://github.com/sola-st/RepairAgent) ![Stars](https://img.shields.io/github/stars/sola-st/RepairAgent?style=social) - 自主 LLM 软件修复代理。

</details>

### 决策引擎

<details>
<summary><b>工具选择</b> — 函数调用与工具使用</summary>

- [gorilla](https://github.com/ShishirPatil/gorilla) ![Stars](https://img.shields.io/github/stars/ShishirPatil/gorilla?style=social) - LLM 函数调用训练与评估。
- [ToolBench](https://github.com/OpenBMB/ToolBench) ![Stars](https://img.shields.io/github/stars/OpenBMB/ToolBench?style=social) - LLM 工具学习开放平台（ICLR 2024 spotlight）。
- [toolformer-pytorch](https://github.com/lucidrains/toolformer-pytorch) ![Stars](https://img.shields.io/github/stars/lucidrains/toolformer-pytorch?style=social) - Toolformer：能使用工具的语言模型。
- [GPTeacher](https://github.com/teknium1/GPTeacher) ![Stars](https://img.shields.io/github/stars/teknium1/GPTeacher?style=social) - 含工具指令的模块化数据集。
- [lemmy](https://github.com/badlogic/lemmy) ![Stars](https://img.shields.io/github/stars/badlogic/lemmy?style=social) - 代理工作流的工具型 LLM 包装器。
- [Hermes-Function-Calling](https://github.com/NousResearch/Hermes-Function-Calling) ![Stars](https://img.shields.io/github/stars/NousResearch/Hermes-Function-Calling?style=social) - 开源 LLM 工具使用微调。
- [ToolAlpaca](https://github.com/tangqiaoyu/ToolAlpaca) ![Stars](https://img.shields.io/github/stars/tangqiaoyu/ToolAlpaca?style=social) - 3000 模拟案例的泛化工具学习。
- [mcp-bench](https://github.com/Accenture/mcp-bench) ![Stars](https://img.shields.io/github/stars/Accenture/mcp-bench?style=social) - 通过 MCP 服务器基准测试工具使用代理。
- [Graph_Toolformer](https://github.com/jwzhanggy/Graph_Toolformer) ![Stars](https://img.shields.io/github/stars/jwzhanggy/Graph_Toolformer?style=social) - 图推理任务的工具增强 LLM。

</details>

<details>
<summary><b>记忆检索</b> — 代理的上下文与记忆管理</summary>

- [mem0](https://github.com/mem0ai/mem0) ![Stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social) - AI 代理通用记忆层。
- [llama_index](https://github.com/run-llama/llama_index) ![Stars](https://img.shields.io/github/stars/run-llama/llama_index?style=social) - 领先的文档代理与检索平台。
- [letta](https://github.com/letta-ai/letta) ![Stars](https://img.shields.io/github/stars/letta-ai/letta?style=social) - 具有高级记忆的有状态代理（原 MemGPT）。
- [haystack](https://github.com/deepset-ai/haystack) ![Stars](https://img.shields.io/github/stars/deepset-ai/haystack?style=social) - AI 编排框架，检索、路由和记忆。
- [txtai](https://github.com/neuml/txtai) ![Stars](https://img.shields.io/github/stars/neuml/txtai?style=social) - 语义搜索与 LLM 工作流一体化框架。
- [zep](https://github.com/getzep/zep) ![Stars](https://img.shields.io/github/stars/getzep/zep?style=social) - AI 助手的长期记忆与上下文管理。
- [langmem](https://github.com/langchain-ai/langmem) ![Stars](https://img.shields.io/github/stars/langchain-ai/langmem?style=social) - LangChain LLM 代理记忆原语。

</details>

<details>
<summary><b>行动优先级排序</b> — 编排与工作流引擎</summary>

- [conductor](https://github.com/conductor-oss/conductor) ![Stars](https://img.shields.io/github/stars/conductor-oss/conductor?style=social) - 事件驱动代理工作流引擎，持久化执行。
- [swarm](https://github.com/openai/swarm) ![Stars](https://img.shields.io/github/stars/openai/swarm?style=social) - 轻量级多代理编排（OpenAI）。
- [agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) ![Stars](https://img.shields.io/github/stars/ComposioHQ/agent-orchestrator?style=social) - 并行编码代理的自主编排。
- [swarms](https://github.com/kyegomez/swarms) ![Stars](https://img.shields.io/github/stars/kyegomez/swarms?style=social) - 企业级多代理编排框架。
- [open-multi-agent](https://github.com/open-multi-agent/open-multi-agent) ![Stars](https://img.shields.io/github/stars/open-multi-agent/open-multi-agent?style=social) - 目标到任务 DAG，TypeScript 多代理编排。
- [mission-control](https://github.com/builderz-labs/mission-control) ![Stars](https://img.shields.io/github/stars/builderz-labs/mission-control?style=social) - 自托管 AI 代理编排平台。
- [agency-swarm](https://github.com/VRSEN/agency-swarm) ![Stars](https://img.shields.io/github/stars/VRSEN/agency-swarm?style=social) - 可靠的多代理编排框架。

</details>

---

## 03. 工具层

### 网络搜索

<details>
<summary><b>网络搜索</b> — 面向 AI 代理的搜索 API 和网页抓取工具</summary>

- [firecrawl](https://github.com/firecrawl/firecrawl) ![Stars](https://img.shields.io/github/stars/firecrawl/firecrawl?style=social) - 为 AI 代理搜索、抓取和清洗网页，将任意网站转为干净的 Markdown。
- [deep-research](https://github.com/dzhng/deep-research) ![Stars](https://img.shields.io/github/stars/dzhng/deep-research?style=social) - AI 驱动的研究助手，结合搜索引擎、网页抓取和大语言模型。
- [DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) ![Stars](https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=social) - 通义深度研究 —— 阿里巴巴开源的深度研究代理。
- [morphic](https://github.com/miurla/morphic) ![Stars](https://img.shields.io/github/stars/miurla/morphic?style=social) - AI 驱动的搜索引擎，带生成式 UI（Perplexity 开源替代）。
- [MiroThinker](https://github.com/MiroMindAI/MiroThinker) ![Stars](https://img.shields.io/github/stars/MiroMindAI/MiroThinker?style=social) - 针对复杂研究和预测任务的深度研究代理。
- [firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) ![Stars](https://img.shields.io/github/stars/firecrawl/firecrawl-mcp-server?style=social) - Firecrawl 官方 MCP 服务器，支持 Cursor、Claude 等 LLM 客户端。
- [open-deep-research](https://github.com/nickscamara/open-deep-research) ![Stars](https://img.shields.io/github/stars/nickscamara/open-deep-research?style=social) - 开源深度研究克隆版，集成 Firecrawl。
- [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) ![Stars](https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=social) - 分层多代理系统，支持自动任务分解的深度研究。
- [tavily-mcp](https://github.com/tavily-ai/tavily-mcp) ![Stars](https://img.shields.io/github/stars/tavily-ai/tavily-mcp?style=social) - 生产就绪的 MCP 服务器，支持实时搜索、提取、映射和爬取。
- [fireplexity](https://github.com/firecrawl/fireplexity) ![Stars](https://img.shields.io/github/stars/firecrawl/fireplexity?style=social) - 开源类 Perplexity AI 搜索引擎，支持实时引用和流式响应。

</details>

### 浏览器自动化

<details>
<summary><b>浏览器自动化</b> — AI 代理的网页浏览和浏览器控制工具</summary>

- [browser-use](https://github.com/browser-use/browser-use) ![Stars](https://img.shields.io/github/stars/browser-use/browser-use?style=social) - 让网站对 AI 代理可访问，轻松自动化在线任务。
- [agent-browser](https://github.com/vercel-labs/agent-browser) ![Stars](https://img.shields.io/github/stars/vercel-labs/agent-browser?style=social) - 面向 AI 代理的浏览器自动化 CLI。
- [agenticSeek](https://github.com/Fosowl/agenticSeek) ![Stars](https://img.shields.io/github/stars/Fosowl/agenticSeek?style=social) - 完全本地化的 Manus AI。能思考、浏览网页和编码的自主代理。
- [nanobrowser](https://github.com/nanobrowser/nanobrowser) ![Stars](https://img.shields.io/github/stars/nanobrowser/nanobrowser?style=social) - 开源 Chrome 扩展，支持 AI 驱动的多代理网页自动化。
- [openbrowser](https://github.com/ntegrals/openbrowser) ![Stars](https://img.shields.io/github/stars/ntegrals/openbrowser?style=social) - 面向浏览器 AI 代理的自主工具包。
- [steel-browser](https://github.com/steel-dev/steel-browser) ![Stars](https://img.shields.io/github/stars/steel-dev/steel-browser?style=social) - 面向 AI 代理的开源浏览器 API，内置浏览器沙箱。
- [LaVague](https://github.com/lavague-ai/LaVague) ![Stars](https://img.shields.io/github/stars/lavague-ai/LaVague?style=social) - 大动作模型框架，用于开发 AI 网页代理。
- [camofox-browser](https://github.com/jo-inc/camofox-browser) ![Stars](https://img.shields.io/github/stars/jo-inc/camofox-browser?style=social) - AI 代理的隐身无头浏览器，可绕过 Cloudflare 机器人检测。
- [openagent](https://github.com/the-open-agent/openagent) ![Stars](https://img.shields.io/github/stars/the-open-agent/openagent?style=social) - 支持 computer-use、browser-use 和编码代理的个人 AI 助手。
- [browser-agent](https://github.com/magnitudedev/browser-agent) ![Stars](https://img.shields.io/github/stars/magnitudedev/browser-agent?style=social) - 开源视觉优先的浏览器代理。

</details>

### 代码执行

<details>
<summary><b>代码执行</b> — AI 代理的沙箱和代码解释器</summary>

- [daytona](https://github.com/daytonaio/daytona) ![Stars](https://img.shields.io/github/stars/daytonaio/daytona?style=social) - 运行 AI 生成代码的安全弹性基础设施。
- [open-interpreter](https://github.com/openinterpreter/open-interpreter) ![Stars](https://img.shields.io/github/stars/openinterpreter/open-interpreter?style=social) - 计算机的自然语言接口，让大语言模型在本地运行代码。
- [E2B](https://github.com/e2b-dev/E2B) ![Stars](https://img.shields.io/github/stars/e2b-dev/E2B?style=social) - 开源安全沙箱云环境，面向企业级 AI 代理。
- [jupyter-ai](https://github.com/jupyterlab/jupyter-ai) ![Stars](https://img.shields.io/github/stars/jupyterlab/jupyter-ai?style=social) - 将 AI 代理连接到 JupyterLab 计算笔记本。
- [judge0](https://github.com/judge0/judge0) ![Stars](https://img.shields.io/github/stars/judge0/judge0?style=social) - 强大、快速、可扩展且沙箱化的在线代码执行系统。
- [arrow-js](https://github.com/standardagents/arrow-js) ![Stars](https://img.shields.io/github/stars/standardagents/arrow-js?style=social) - 代理时代的 UI 框架，使用 WASM 沙箱安全执行代码。
- [code-interpreter](https://github.com/e2b-dev/code-interpreter) ![Stars](https://img.shields.io/github/stars/e2b-dev/code-interpreter?style=social) - 在 AI 应用中运行 AI 生成代码的 Python 和 JS/TS SDK。
- [dify-sandbox](https://github.com/langgenius/dify-sandbox) ![Stars](https://img.shields.io/github/stars/langgenius/dify-sandbox?style=social) - 轻量、快速且安全的代码执行环境（Dify 团队出品）。
- [arrakis](https://github.com/abshkbh/arrakis) ![Stars](https://img.shields.io/github/stars/abshkbh/arrakis?style=social) - 自托管的 AI 代理代码执行沙箱，支持 MicroVM 隔离。
- [SmolVM](https://github.com/CelestoAI/SmolVM) ![Stars](https://img.shields.io/github/stars/CelestoAI/SmolVM?style=social) - 开源 AI 沙箱基础设施，支持代码执行、浏览器使用和 AI 代理。

</details>

### API 集成

<details>
<summary><b>API 集成</b> — MCP 服务器、工具连接器和代理 API 框架</summary>

- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) ![Stars](https://img.shields.io/github/stars/punkpeye/awesome-mcp-servers?style=social) - 精选 MCP 服务器合集。
- [servers](https://github.com/modelcontextprotocol/servers) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=social) - Model Context Protocol 官方参考服务器。
- [playwright-mcp](https://github.com/microsoft/playwright-mcp) ![Stars](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=social) - Playwright MCP 服务器 —— AI 代理的浏览器自动化。
- [github-mcp-server](https://github.com/github/github-mcp-server) ![Stars](https://img.shields.io/github/stars/github/github-mcp-server?style=social) - GitHub 官方 MCP 服务器，用于 AI 代理集成。
- [fastmcp](https://github.com/PrefectHQ/fastmcp) ![Stars](https://img.shields.io/github/stars/PrefectHQ/fastmcp?style=social) - 快速、Pythonic 的 MCP 服务器和客户端构建方式。
- [python-sdk](https://github.com/modelcontextprotocol/python-sdk) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/python-sdk?style=social) - MCP 服务器和客户端的官方 Python SDK。
- [activepieces](https://github.com/activepieces/activepieces) ![Stars](https://img.shields.io/github/stars/activepieces/activepieces?style=social) - AI 代理、MCP 和 AI 工作流自动化（约 400 个 MCP 服务器）。
- [mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) ![Stars](https://img.shields.io/github/stars/microsoft/mcp-for-beginners?style=social) - 开源 MCP 课程，含多语言示例。
- [mcp-toolbox](https://github.com/googleapis/mcp-toolbox) ![Stars](https://img.shields.io/github/stars/googleapis/mcp-toolbox?style=social) - Google 开源的数据库 MCP 服务器。
- [Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) ![Stars](https://img.shields.io/github/stars/GLips/Figma-Context-MCP?style=social) - 向 AI 编码代理提供 Figma 布局信息的 MCP 服务器。

</details>

### 数据库访问

<details>
<summary><b>数据库访问</b> — Text-to-SQL、数据库代理和 NL2SQL 工具</summary>

- [vanna](https://github.com/vanna-ai/vanna) ![Stars](https://img.shields.io/github/stars/vanna-ai/vanna?style=social) - 与 SQL 数据库对话。基于大语言模型的 Agentic RAG 精准 Text-to-SQL。
- [WrenAI](https://github.com/Canner/WrenAI) ![Stars](https://img.shields.io/github/stars/Canner/WrenAI?style=social) - 将 AI 代理变为数据分析专家。支持 20+ 数据源的 Text-to-SQL 和分析。
- [SQLBot](https://github.com/dataease/SQLBot) ![Stars](https://img.shields.io/github/stars/dataease/SQLBot?style=social) - 基于大语言模型和 RAG 的智能数据查询系统。
- [Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL) ![Stars](https://img.shields.io/github/stars/eosphoros-ai/Awesome-Text2SQL?style=social) - Text2SQL、Text2DSL、Text2API、Text2SQL 精选教程和资源。
- [DB-GPT-Hub](https://github.com/eosphoros-ai/DB-GPT-Hub) ![Stars](https://img.shields.io/github/stars/eosphoros-ai/DB-GPT-Hub?style=social) - Text-to-SQL 模型、数据集和微调技术。
- [NL2SQL](https://github.com/yechens/NL2SQL) ![Stars](https://img.shields.io/github/stars/yechens/NL2SQL?style=social) - Text2SQL 语义解析数据集、解决方案和论文资源。
- [NL2SQL_Handbook](https://github.com/HKUSTDial/NL2SQL_Handbook) ![Stars](https://img.shields.io/github/stars/HKUSTDial/NL2SQL_Handbook?style=social) - 持续更新的 Text-to-SQL 技术手册。
- [Awesome-LLM-based-Text2SQL](https://github.com/DEEP-PolyU/Awesome-LLM-based-Text2SQL) ![Stars](https://img.shields.io/github/stars/DEEP-PolyU/Awesome-LLM-based-Text2SQL?style=social) - TKDE 2025 综述：下一代数据库接口。
- [spider](https://github.com/taoyds/spider) ![Stars](https://img.shields.io/github/stars/taoyds/spider?style=social) - Yale 跨域语义解析和 text-to-SQL 挑战赛基准。
- [BIRD-Interact](https://github.com/bird-bench/BIRD-Interact) ![Stars](https://img.shields.io/github/stars/bird-bench/BIRD-Interact?style=social) - ICLR 2026 Oral。通过动态交互重新定义 Text-to-SQL 评估。

</details>

### 文件系统

<details>
<summary><b>文件系统</b> — 文档处理、解析和非结构化数据工具</summary>

- [marker](https://github.com/datalab-to/marker) ![Stars](https://img.shields.io/github/stars/datalab-to/marker?style=social) - 高精度快速将 PDF 转换为 Markdown + JSON。
- [MonkeyOCR](https://github.com/Yuliang-Liu/MonkeyOCR) ![Stars](https://img.shields.io/github/stars/Yuliang-Liu/MonkeyOCR?style=social) - 轻量级 LMM 文档解析模型。
- [unstract](https://github.com/Zipstack/unstract) ![Stars](https://img.shields.io/github/stars/Zipstack/unstract?style=social) - 大语言模型驱动的非结构化数据提取，支持 API 部署和 ETL 管道。
- [liteparse](https://github.com/run-llama/liteparse) ![Stars](https://img.shields.io/github/stars/run-llama/liteparse?style=social) - 快速、好用的开源文档解析器（LlamaIndex 团队出品）。
- [llm-graph-builder](https://github.com/neo4j-labs/llm-graph-builder) ![Stars](https://img.shields.io/github/stars/neo4j-labs/llm-graph-builder?style=social) - 使用大语言模型从非结构化数据构建 Neo4j 图谱。
- [datachain](https://github.com/datachain-ai/datachain) ![Stars](https://img.shields.io/github/stars/datachain-ai/datachain?style=social) - 非结构化数据的上下文层：支持 S3、GCS、Azure 的类型化版本化数据集。
- [OCRFlux](https://github.com/chatdoc-com/OCRFlux) ![Stars](https://img.shields.io/github/stars/chatdoc-com/OCRFlux?style=social) - PDF 转 Markdown 的多模态工具包，支持复杂布局和表格解析。
- [docext](https://github.com/NanoNets/docext) ![Stars](https://img.shields.io/github/stars/NanoNets/docext?style=social) - 本地部署、无需 OCR 的非结构化数据提取和 Markdown 转换工具包。
- [semtools](https://github.com/run-llama/semtools) ![Stars](https://img.shields.io/github/stars/run-llama/semtools?style=social) - 命令行语义搜索和文档解析工具。
- [OmniDocBench](https://github.com/opendatalab/OmniDocBench) ![Stars](https://img.shields.io/github/stars/opendatalab/OmniDocBench?style=social) - CVPR 2025 —— 文档解析和评估的综合基准。

</details>

---

## 04. 代理工作流

### 研究代理

<details>
<summary><b>研究代理</b> — 自动化研究、深度研究和论文发现代理</summary>

- [storm](https://github.com/stanford-oval/storm) ![Stars](https://img.shields.io/github/stars/stanford-oval/storm?style=social) - 大语言模型驱动的知识策展系统，研究主题并生成带引用的完整报告。
- [gpt-researcher](https://github.com/assafelovic/gpt-researcher) ![Stars](https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=social) - 自主代理，使用任意大语言模型对任何主题进行深度研究。
- [deep-research](https://github.com/dzhng/deep-research) ![Stars](https://img.shields.io/github/stars/dzhng/deep-research?style=social) - 结合搜索引擎、网页抓取和大语言模型的 AI 研究助手。
- [DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) ![Stars](https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=social) - 通义深度研究 —— 阿里巴巴开源的深度研究代理。
- [MiroThinker](https://github.com/MiroMindAI/MiroThinker) ![Stars](https://img.shields.io/github/stars/MiroMindAI/MiroThinker?style=social) - 针对复杂研究和预测任务的深度研究代理。
- [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) ![Stars](https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=social) - 支持自动任务分解的分层多代理深度研究系统。
- [ai-research-assistant](https://github.com/lifan0127/ai-research-assistant) ![Stars](https://img.shields.io/github/stars/lifan0127/ai-research-assistant?style=social) - Aria：基于 GPT 大语言模型的 AI 研究助手。
- [NanoResearch](https://github.com/OpenRaiser/NanoResearch) ![Stars](https://img.shields.io/github/stars/OpenRaiser/NanoResearch?style=social) - 自主 AI 研究助手。
- [DeepGit](https://github.com/zamalali/DeepGit) ![Stars](https://img.shields.io/github/stars/zamalali/DeepGit?style=social) - 帮助寻找最佳 GitHub 仓库的深度研究代理。
- [deep_research_bench](https://github.com/Ayanami0730/deep_research_bench) ![Stars](https://img.shields.io/github/stars/Ayanami0730/deep_research_bench?style=social) - 深度研究代理综合基准测试。

</details>

### 编码代理

<details>
<summary><b>编码代理</b> — 自主编码和软件工程代理</summary>

- [opencode](https://github.com/anomalyco/opencode) ![Stars](https://img.shields.io/github/stars/anomalyco/opencode?style=social) - 开源编码代理。
- [claude-code](https://github.com/anthropics/claude-code) ![Stars](https://img.shields.io/github/stars/anthropics/claude-code?style=social) - 终端中的智能编码工具，理解你的代码库。
- [codex](https://github.com/openai/codex) ![Stars](https://img.shields.io/github/stars/openai/codex?style=social) - 在终端中运行的轻量级编码代理。
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) ![Stars](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=social) - AI 驱动的开发平台。
- [cline](https://github.com/cline/cline) ![Stars](https://img.shields.io/github/stars/cline/cline?style=social) - 作为 SDK、IDE 扩展或 CLI 助手的自主编码代理。
- [aider](https://github.com/Aider-AI/aider) ![Stars](https://img.shields.io/github/stars/Aider-AI/aider?style=social) - 终端中的 AI 结对编程。
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) ![Stars](https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=social) - 接收 GitHub issue 并尝试自动修复（NeurIPS 2024）。
- [DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) ![Stars](https://img.shields.io/github/stars/Hmbown/DeepSeek-TUI?style=social) - 在终端中运行的 DeepSeek 模型编码代理。
- [claude-coder](https://github.com/kodu-ai/claude-coder) ![Stars](https://img.shields.io/github/stars/kodu-ai/claude-coder?style=social) - 住在 IDE 中的自主编码代理（VSCode 扩展）。
- [OpenAlpha_Evolve](https://github.com/shyamsaktawat/OpenAlpha_Evolve) ![Stars](https://img.shields.io/github/stars/shyamsaktawat/OpenAlpha_Evolve?style=social) - 受 DeepMind AlphaEvolve 启发的自主编码框架。

</details>

### 销售代理

<details>
<summary><b>销售代理</b> — 销售自动化、外呼和潜在客户挖掘代理</summary>

- [SalesGPT](https://github.com/filip-michalsky/SalesGPT) ![Stars](https://img.shields.io/github/stars/filip-michalsky/SalesGPT?style=social) - 具有上下文感知的 AI 销售代理，自动化销售外呼。
- [Knotie-AI](https://github.com/avijeett007/Knotie-AI) ![Stars](https://img.shields.io/github/stars/avijeett007/Knotie-AI?style=social) - 开源的呼入/呼出 AI 销售代理。
- [b2b-sdr-agent-template](https://github.com/iPythoning/b2b-sdr-agent-template) ![Stars](https://img.shields.io/github/stars/iPythoning/b2b-sdr-agent-template?style=social) - B2B 开源 AI SDR 模板：10 阶段管道，多渠道触达。
- [sales-ai-agent-langgraph](https://github.com/lucasboscatti/sales-ai-agent-langgraph) ![Stars](https://img.shields.io/github/stars/lucasboscatti/sales-ai-agent-langgraph?style=social) - 使用 LangChain、LangGraph 和 Gemini Flash 的虚拟销售代理。
- [AI-Sales-agent](https://github.com/kaymen99/AI-Sales-agent) ![Stars](https://img.shields.io/github/stars/kaymen99/AI-Sales-agent?style=social) - 带产品推荐、咨询和 Stripe 支付的销售 AI 代理。
- [cold-email-ai](https://github.com/bdcorps/cold-email-ai) ![Stars](https://img.shields.io/github/stars/bdcorps/cold-email-ai?style=social) - AI 驱动的冷邮件生成和外呼系统。
- [SalesAgent](https://github.com/MiuLab/SalesAgent) ![Stars](https://img.shields.io/github/stars/MiuLab/SalesAgent?style=social) - SalesBot 2.0 — 研究导向的 AI 销售对话代理。

</details>

### 客户支持代理

<details>
<summary><b>客户支持代理</b> — 帮助台、聊天机器人和客服代理</summary>

- [Flowise](https://github.com/FlowiseAI/Flowise) ![Stars](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=social) - 可视化构建 AI 代理。拖放式大语言模型聊天机器人和代理平台。
- [chatwoot](https://github.com/chatwoot/chatwoot) ![Stars](https://img.shields.io/github/stars/chatwoot/chatwoot?style=social) - 开源全渠道客户支持平台。Intercom、Zendesk 的替代方案。
- [rasa](https://github.com/RasaHQ/rasa) ![Stars](https://img.shields.io/github/stars/RasaHQ/rasa?style=social) - 开源 ML 框架，用于文本和语音对话 AI。
- [botpress](https://github.com/botpress/botpress) ![Stars](https://img.shields.io/github/stars/botpress/botpress?style=social) - 构建和部署 GPT/LLM 对话代理的开源中心。
- [cossistant](https://github.com/cossistantcom/cossistant) ![Stars](https://img.shields.io/github/stars/cossistantcom/cossistant?style=social) - 开源客户支持平台，支持可定制的 AI 支持代理。
- [tiledesk-server](https://github.com/Tiledesk/tiledesk-server) ![Stars](https://img.shields.io/github/stars/Tiledesk/tiledesk-server?style=social) - Voiceflow 的开源替代方案，支持大语言模型代理和人工参与。

</details>

### 内容代理

<details>
<summary><b>内容代理</b> — 内容生成、写作和创意代理</summary>

- [xhs_content_agent](https://github.com/hl897tech/xhs_content_agent) ![Stars](https://img.shields.io/github/stars/hl897tech/xhs_content_agent?style=social) - 基于大语言模型的小红书内容运营代理：趋势分析、文案生成、图片制作和发布。
- [ai-creator](https://github.com/gongxings/ai-creator) ![Stars](https://img.shields.io/github/stars/gongxings/ai-creator?style=social) - AI 内容创作平台，支持写作、图片、视频、PPT 生成和多平台发布。
- [sage-x-agent](https://github.com/sharbelxyz/sage-x-agent) ![Stars](https://img.shields.io/github/stars/sharbelxyz/sage-x-agent?style=social) - X (Twitter) 内容代理：语调校准、推文撰写、话题串写作和趋势监测。
- [blog-writing-agent](https://github.com/campusx-official/blog-writing-agent) ![Stars](https://img.shields.io/github/stars/campusx-official/blog-writing-agent?style=social) - 基于 LangGraph 的博客写作代理。
- [video-content-agent](https://github.com/sailorworks/video-content-agent) ![Stars](https://img.shields.io/github/stars/sailorworks/video-content-agent?style=social) - 将话题转化为爆款短视频的端到端 AI 代理。
- [content-agent](https://github.com/qiuxchao/content-agent) ![Stars](https://img.shields.io/github/stars/qiuxchao/content-agent?style=social) - 自动搜索素材，为微信/小红书/知乎生成文章。基于 LangGraph。
- [citedy-seo-agent](https://github.com/citedy/citedy-seo-agent) ![Stars](https://img.shields.io/github/stars/citedy/citedy-seo-agent?style=social) - AI 驱动的 SEO 内容自动化：趋势监测、55 种语言文章生成。

</details>

### 自主工作流

<details>
<summary><b>自主工作流</b> — 通用自主代理平台和工作流引擎</summary>

- [dify](https://github.com/langgenius/dify) ![Stars](https://img.shields.io/github/stars/langgenius/dify?style=social) - 生产就绪的代理工作流开发平台，支持编排、RAG 和代理。
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) ![Stars](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT?style=social) - 实验性开源自主 AI 代理 —— 最初的 AutoGPT。
- [conductor](https://github.com/conductor-oss/conductor) ![Stars](https://img.shields.io/github/stars/conductor-oss/conductor?style=social) - 事件驱动的代理工作流引擎，支持持久弹性执行。
- [openai-agents-python](https://github.com/openai/openai-agents-python) ![Stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=social) - 轻量强大的多代理工作流框架（OpenAI Agents SDK）。
- [haystack](https://github.com/deepset-ai/haystack) ![Stars](https://img.shields.io/github/stars/deepset-ai/haystack?style=social) - 开源 AI 编排框架，用于上下文工程化的大语言模型应用。
- [opik](https://github.com/comet-ml/opik) ![Stars](https://img.shields.io/github/stars/comet-ml/opik?style=social) - 调试、评估和监控大语言模型应用和代理工作流。
- [agent-framework](https://github.com/microsoft/agent-framework) ![Stars](https://img.shields.io/github/stars/microsoft/agent-framework?style=social) - 构建、编排和部署 AI 代理的框架（Python 和 .NET）。

</details>

---

## 05. 多代理系统

### 管理代理

<details>
<summary><b>管理代理</b> — 多代理系统的编排、监督和路由模式</summary>

- [autogen](https://github.com/microsoft/autogen) ![Stars](https://img.shields.io/github/stars/microsoft/autogen?style=social) - 多代理对话和编排的智能 AI 编程框架。
- [crewAI](https://github.com/crewAIInc/crewAI) ![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=social) - 编排角色扮演自主 AI 代理的框架。
- [agno](https://github.com/agno-agi/agno) ![Stars](https://img.shields.io/github/stars/agno-agi/agno?style=social) - 构建和运行代理平台，支持多代理编排（原名 Phidata）。
- [langgraph](https://github.com/langchain-ai/langgraph) ![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social) - 基于图的代理编排，支持监督者/集群模式。
- [semantic-kernel](https://github.com/microsoft/semantic-kernel) ![Stars](https://img.shields.io/github/stars/microsoft/semantic-kernel?style=social) - 将大语言模型集成到应用中，支持多代理编排（Handoff、Supervisor）。
- [openai-agents-python](https://github.com/openai/openai-agents-python) ![Stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=social) - 轻量级多代理框架，支持交接和编排。
- [adk-python](https://github.com/google/adk-python) ![Stars](https://img.shields.io/github/stars/google/adk-python?style=social) - Google 代码优先的 Python 工具包，用于构建多代理系统。
- [camel](https://github.com/camel-ai/camel) ![Stars](https://img.shields.io/github/stars/camel-ai/camel?style=social) - 基于角色的多代理编排框架。
- [swarms](https://github.com/kyegomez/swarms) ![Stars](https://img.shields.io/github/stars/kyegomez/swarms?style=social) - 企业级生产就绪的多代理编排框架。
- [sdk-python](https://github.com/strands-agents/sdk-python) ![Stars](https://img.shields.io/github/stars/strands-agents/sdk-python?style=social) - 模型驱动的 AI 代理构建方法，支持多代理模式。

</details>

### 工作者代理

<details>
<summary><b>工作者代理</b> — 任务执行、并行处理和分布式代理</summary>

- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) ![Stars](https://img.shields.io/github/stars/FoundationAgents/MetaGPT?style=social) - 多代理框架，分配专业工作者角色（PM、架构师、工程师、QA）。
- [ChatDev](https://github.com/OpenBMB/ChatDev) ![Stars](https://img.shields.io/github/stars/OpenBMB/ChatDev?style=social) - 多代理协作，代理担任专业角色（CEO、CTO、程序员、测试员、设计师）。
- [agentscope](https://github.com/agentscope-ai/agentscope) ![Stars](https://img.shields.io/github/stars/agentscope-ai/agentscope?style=social) - 构建分布式多代理系统，支持可定制技能。
- [AgentVerse](https://github.com/OpenBMB/AgentVerse) ![Stars](https://img.shields.io/github/stars/OpenBMB/AgentVerse?style=social) - 部署具有不同专业化的多代理系统用于任务解决。

</details>

### 审查代理

<details>
<summary><b>审查代理</b> — 代码审查、质量保证和批评代理</summary>

- [pr-agent](https://github.com/The-PR-Agent/pr-agent) ![Stars](https://img.shields.io/github/stars/The-PR-Agent/pr-agent?style=social) - 开源 AI PR 审查代理，自动化代码审查和改进建议。
- [agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) ![Stars](https://img.shields.io/github/stars/ComposioHQ/agent-orchestrator?style=social) - 并行编码代理，自动处理 CI 修复、合并冲突和代码审查。
- [shippie](https://github.com/mattzcarey/shippie) ![Stars](https://img.shields.io/github/stars/mattzcarey/shippie?style=social) - 可扩展的代码审查和 QA 代理。
- [ai-devkit](https://github.com/codeaholicguy/ai-devkit) ![Stars](https://img.shields.io/github/stars/codeaholicguy/ai-devkit?style=social) - AI 编码代理，含规划、记忆和审查的工程工作流。
- [claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) ![Stars](https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=social) - Claude Code 模板，含多代理审查、质量门禁和对抗性 QA。
- [sashiko](https://github.com/sashiko-dev/sashiko) ![Stars](https://img.shields.io/github/stars/sashiko-dev/sashiko?style=social) - Linux 内核补丁的大语言模型代码审查代理。
- [awesome-reviewers](https://github.com/baz-scm/awesome-reviewers) ![Stars](https://img.shields.io/github/stars/baz-scm/awesome-reviewers?style=social) - 代理代码审查系统提示词精选集。

</details>

### 专业技能

<details>
<summary><b>专业技能</b> — 领域特定和专家代理</summary>

- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) ![Stars](https://img.shields.io/github/stars/FoundationAgents/MetaGPT?style=social) - 多代理框架，支持专业角色（PM、架构师、工程师、QA）。
- [ChatDev](https://github.com/OpenBMB/ChatDev) ![Stars](https://img.shields.io/github/stars/OpenBMB/ChatDev?style=social) - 代理担任专业角色（CEO、CTO、程序员、测试员、设计师）。
- [agentscope](https://github.com/agentscope-ai/agentscope) ![Stars](https://img.shields.io/github/stars/agentscope-ai/agentscope?style=social) - 分布式专业代理，支持可定制技能。
- [AgentVerse](https://github.com/OpenBMB/AgentVerse) ![Stars](https://img.shields.io/github/stars/OpenBMB/AgentVerse?style=social) - 部署不同专业化的代理用于任务解决和模拟。
- [camel](https://github.com/camel-ai/camel) ![Stars](https://img.shields.io/github/stars/camel-ai/camel?style=social) - 多代理框架中的角色扮演专业代理。

</details>

### 共享内存总线

<details>
<summary><b>共享内存总线</b> — 多代理系统的通信、消息传递和共享内存</summary>

- [omem](https://github.com/ourmem/omem) ![Stars](https://img.shields.io/github/stars/ourmem/omem?style=social) - 永不遗忘的共享内存 — 支持代理和团队的 Space 级别共享持久内存。
- [eion](https://github.com/eiondb/eion) ![Stars](https://img.shields.io/github/stars/eiondb/eion?style=social) - 多代理系统的共享内存存储。
- [stash](https://github.com/Fergana-Labs/stash) ![Stars](https://img.shields.io/github/stars/Fergana-Labs/stash?style=social) - 团队编码代理的共享内存。
- [memX](https://github.com/MehulG/memX) ![Stars](https://img.shields.io/github/stars/MehulG/memX?style=social) - 多代理大语言模型系统的实时共享内存层。
- [llegos](https://github.com/CyrusNuevoDia/llegos) ![Stars](https://img.shields.io/github/stars/CyrusNuevoDia/llegos?style=social) - 强类型 Python DSL，用于消息传递多代理系统。
- [ALMA-memory](https://github.com/RBKunnela/ALMA-memory) ![Stars](https://img.shields.io/github/stars/RBKunnela/ALMA-memory?style=social) - AI 代理持久内存，支持范围学习和多代理共享。

</details>

---

## 06. 基础设施

### LangGraph

<details>
<summary><b>LangGraph</b> — 基于 LangChain 的有状态多参与者代理编排</summary>

- [langchain](https://github.com/langchain-ai/langchain) ![Stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=social) - 代理工程平台（LangGraph 为核心子项目）。
- [deer-flow](https://github.com/bytedance/deer-flow) ![Stars](https://img.shields.io/github/stars/bytedance/deer-flow?style=social) - 字节跳动基于 LangGraph 的开源 SuperAgent 框架。
- [langgraph](https://github.com/langchain-ai/langgraph) ![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social) - LangGraph 官方库，用于有状态多参与者代理编排。
- [deepagents](https://github.com/langchain-ai/deepagents) ![Stars](https://img.shields.io/github/stars/langchain-ai/deepagents?style=social) - 基于 LangGraph 的全功能代理框架。
- [GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) ![Stars](https://img.shields.io/github/stars/NirDiamant/GenAI_Agents?style=social) - 50+ 生成式 AI 代理技术教程和实现。
- [agents-towards-production](https://github.com/NirDiamant/agents-towards-production) ![Stars](https://img.shields.io/github/stars/NirDiamant/agents-towards-production?style=social) - 构建生产级 GenAI 代理的端到端教程。
- [gemini-fullstack-langgraph-quickstart](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart) ![Stars](https://img.shields.io/github/stars/google-gemini/gemini-fullstack-langgraph-quickstart?style=social) - 使用 Gemini 2.5 和 LangGraph 构建全栈代理。
- [SurfSense](https://github.com/MODSetter/SurfSense) ![Stars](https://img.shields.io/github/stars/MODSetter/SurfSense?style=social) - 开源隐私优先的 NotebookLM 替代方案，基于 LangGraph。

</details>

### CrewAI

<details>
<summary><b>CrewAI</b> — 角色扮演自主 AI 代理编排</summary>

- [crewAI](https://github.com/crewAIInc/crewAI) ![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=social) - 编排角色扮演自主 AI 代理的框架。
- [crewAI-examples](https://github.com/crewAIInc/crewAI-examples) ![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI-examples?style=social) - CrewAI 工作流官方示例集合。
- [crewAI-tools](https://github.com/crewAIInc/crewAI-tools) ![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI-tools?style=social) - 扩展 CrewAI 代理的官方工具库。
- [CrewAI-Studio](https://github.com/strnad/CrewAI-Studio) ![Stars](https://img.shields.io/github/stars/strnad/CrewAI-Studio?style=social) - 管理和运行 CrewAI 代理的友好 GUI。
- [full-stack-ai-agent-template](https://github.com/vstorm-co/full-stack-ai-agent-template) ![Stars](https://img.shields.io/github/stars/vstorm-co/full-stack-ai-agent-template?style=social) - 全栈 AI 应用生成器（FastAPI + Next.js），集成 CrewAI。

</details>

### OpenAI Agents SDK

<details>
<summary><b>OpenAI Agents SDK</b> — OpenAI 官方多代理框架</summary>

- [openai-agents-python](https://github.com/openai/openai-agents-python) ![Stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=social) - 轻量强大的多代理工作流框架（Python）。
- [swarm](https://github.com/openai/swarm) ![Stars](https://img.shields.io/github/stars/openai/swarm?style=social) - 探索轻量级多代理编排的教育框架。
- [openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) ![Stars](https://img.shields.io/github/stars/openai/openai-cs-agents-demo?style=social) - 使用 OpenAI Agents SDK 的客户服务演示。
- [openai-agents-js](https://github.com/openai/openai-agents-js) ![Stars](https://img.shields.io/github/stars/openai/openai-agents-js?style=social) - 官方 JS/TS 多代理工作流和语音代理 SDK。
- [learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) ![Stars](https://img.shields.io/github/stars/panaversity/learn-agentic-ai?style=social) - 使用 OpenAI Agents SDK、MCP、A2A 和 Kubernetes 学习代理式 AI。
- [agents-deep-research](https://github.com/qx-labs/agents-deep-research) ![Stars](https://img.shields.io/github/stars/qx-labs/agents-deep-research?style=social) - 使用 OpenAI Agents SDK 实现迭代深度研究。

</details>

### MCP

<details>
<summary><b>MCP（模型上下文协议）</b> — 大语言模型与工具集成的标准协议</summary>

- [servers](https://github.com/modelcontextprotocol/servers) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=social) - Model Context Protocol 官方参考服务器实现。
- [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) ![Stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=social) - 通过 MCP 将 Chrome DevTools 暴露给编码代理。
- [playwright-mcp](https://github.com/microsoft/playwright-mcp) ![Stars](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=social) - Playwright MCP 服务器 —— AI 代理的浏览器自动化。
- [fastmcp](https://github.com/PrefectHQ/fastmcp) ![Stars](https://img.shields.io/github/stars/PrefectHQ/fastmcp?style=social) - 快速、Pythonic 的 MCP 服务器和客户端构建方式。
- [python-sdk](https://github.com/modelcontextprotocol/python-sdk) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/python-sdk?style=social) - MCP 服务器和客户端的官方 Python SDK。
- [typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/typescript-sdk?style=social) - MCP 服务器和客户端的官方 TypeScript SDK。
- [fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) ![Stars](https://img.shields.io/github/stars/tadata-org/fastapi_mcp?style=social) - 将 FastAPI 端点暴露为 MCP 工具（含认证）。
- [mcp-go](https://github.com/mark3labs/mcp-go) ![Stars](https://img.shields.io/github/stars/mark3labs/mcp-go?style=social) - Go 语言的 Model Context Protocol 实现。
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) ![Stars](https://img.shields.io/github/stars/lastmile-ai/mcp-agent?style=social) - 使用 MCP 和工作流模式构建高效代理。
- [modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/modelcontextprotocol?style=social) - MCP 规范和文档。

</details>

### Docker

<details>
<summary><b>Docker</b> — 容器化代理部署和管理</summary>

- [dify](https://github.com/langgenius/dify) ![Stars](https://img.shields.io/github/stars/langgenius/dify?style=social) - 生产就绪的代理平台，Docker 优先部署（docker-compose）。
- [OpenHands](https://github.com/OpenHands/OpenHands) ![Stars](https://img.shields.io/github/stars/OpenHands/OpenHands?style=social) - AI 驱动的开发平台，代理在 Docker 沙箱容器中运行。
- [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) ![Stars](https://img.shields.io/github/stars/Pythagora-io/gpt-pilot?style=social) - AI 开发者，使用 Docker 容器进行隔离代码执行和测试。
- [agent-zero](https://github.com/agent0ai/agent-zero) ![Stars](https://img.shields.io/github/stars/agent0ai/agent-zero?style=social) - 基于 Docker 的多代理系统，支持容器化工具执行。
- [text-generation-inference](https://github.com/huggingface/text-generation-inference) ![Stars](https://img.shields.io/github/stars/huggingface/text-generation-inference?style=social) - Docker 容器化的大语言模型推理服务基础设施。
- [llama_deploy](https://github.com/run-llama/llama_deploy) ![Stars](https://img.shields.io/github/stars/run-llama/llama_deploy?style=social) - 将代理工作流部署到生产环境的容器感知部署基础设施。

</details>

### Kubernetes

<details>
<summary><b>Kubernetes</b> — K8s 上的可扩展代理编排</summary>

- [k8sgpt](https://github.com/k8sgpt-ai/k8sgpt) ![Stars](https://img.shields.io/github/stars/k8sgpt-ai/k8sgpt?style=social) - 为每个人赋予 Kubernetes 超能力 — AI 驱动的 K8s 诊断和 SRE。
- [kubectl-ai](https://github.com/GoogleCloudPlatform/kubectl-ai) ![Stars](https://img.shields.io/github/stars/GoogleCloudPlatform/kubectl-ai?style=social) - AI 驱动的 Kubernetes 助手 — 通过大语言模型代理实现自然语言到 kubectl。
- [kagent](https://github.com/kagent-dev/kagent) ![Stars](https://img.shields.io/github/stars/kagent-dev/kagent?style=social) - 云原生代理式 AI — 在 Kubernetes 上运行和编排 AI 代理。
- [dstack](https://github.com/dstackai/dstack) ![Stars](https://img.shields.io/github/stars/dstackai/dstack?style=social) - 供应商无关的 K8s 上 AI 训练、推理和代理工作负载编排。
- [kubeai](https://github.com/kubeai-project/kubeai) ![Stars](https://img.shields.io/github/stars/kubeai-project/kubeai?style=social) - Kubernetes AI 推理 Operator — 生产环境 ML 模型服务的最简方式。
- [kubectl-ai](https://github.com/sozercan/kubectl-ai) ![Stars](https://img.shields.io/github/stars/sozercan/kubectl-ai?style=social) - Kubectl 插件，使用大语言模型创建清单 — AI 生成的 K8s 资源。
- [k8sgpt-operator](https://github.com/k8sgpt-ai/k8sgpt-operator) ![Stars](https://img.shields.io/github/stars/k8sgpt-ai/k8sgpt-operator?style=social) - Kubernetes 集群内的自动 SRE 超能力 — k8sgpt 的 operator。
- [arcadia](https://github.com/kubeagi/arcadia) ![Stars](https://img.shields.io/github/stars/kubeagi/arcadia?style=social) - Kubernetes 上多样化、简单且安全的一体化 LLMOps 平台。

**相关 K8s AI 服务基础设施：** [kubeflow](https://github.com/kubeflow/kubeflow)（K8s ML 工具包）、[kserve](https://github.com/kserve/kserve)（标准化 AI 推理）、[llm-d](https://github.com/llm-d/llm-d)（K8s 上的最先进 LLM 推理）。

</details>

---

## 07. 可观测性

### 日志

<details>
<summary><b>日志</b> — 大语言模型和代理的日志、监控和可观测性平台</summary>

- [langfuse](https://github.com/langfuse/langfuse) ![Stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social) - 开源大语言模型工程平台：可观测性、指标、评估和提示管理。
- [mlflow](https://github.com/mlflow/mlflow) ![Stars](https://img.shields.io/github/stars/mlflow/mlflow?style=social) - 开源 AI 工程平台，支持代理、大语言模型和 ML 模型的追踪和成本控制。
- [opik](https://github.com/comet-ml/opik) ![Stars](https://img.shields.io/github/stars/comet-ml/opik?style=social) - 调试、评估和监控大语言模型应用和代理工作流。
- [openobserve](https://github.com/openobserve/openobserve) ![Stars](https://img.shields.io/github/stars/openobserve/openobserve?style=social) - 开源可观测性平台，支持日志、指标、追踪和大语言模型可观测性。
- [RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) ![Stars](https://img.shields.io/github/stars/raga-ai-hub/RagaAI-Catalyst?style=social) - 代理 AI 可观测性：追踪、调试多代理系统，含时间线和执行图。
- [phoenix](https://github.com/Arize-ai/phoenix) ![Stars](https://img.shields.io/github/stars/Arize-ai/phoenix?style=social) - AI 可观测性和评估：大语言模型应用的追踪、评估和调试。
- [openllmetry](https://github.com/traceloop/openllmetry) ![Stars](https://img.shields.io/github/stars/traceloop/openllmetry?style=social) - 基于 OpenTelemetry 的开源 GenAI/LLM 可观测性。
- [helicone](https://github.com/Helicone/helicone) ![Stars](https://img.shields.io/github/stars/Helicone/helicone?style=social) - 开源大语言模型可观测性 — 一行代码即可监控、评估和实验。
- [agentops](https://github.com/AgentOps-AI/agentops) ![Stars](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=social) - AI 代理监控和大语言模型成本追踪 Python SDK。
- [logfire](https://github.com/pydantic/logfire) ![Stars](https://img.shields.io/github/stars/pydantic/logfire?style=social) - 生产级大语言模型和代理系统的 AI 可观测性平台（Pydantic 团队）。

</details>

### 追踪

<details>
<summary><b>追踪</b> — 大语言模型遥测、分布式追踪和请求跟踪</summary>

- [langfuse](https://github.com/langfuse/langfuse) ![Stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social) - 大语言模型工程平台，支持全面的追踪（OpenTelemetry、Langchain、OpenAI SDK）。
- [opik](https://github.com/comet-ml/opik) ![Stars](https://img.shields.io/github/stars/comet-ml/opik?style=social) - 大语言模型/代理工作流的全面追踪和自动评估。
- [gateway](https://github.com/Portkey-AI/gateway) ![Stars](https://img.shields.io/github/stars/Portkey-AI/gateway?style=social) - 极速 AI 网关，集成护栏，路由到 1600+ 大语言模型。
- [phoenix](https://github.com/Arize-ai/phoenix) ![Stars](https://img.shields.io/github/stars/Arize-ai/phoenix?style=social) - 大语言模型/代理工作流的追踪、评估和实验。
- [openllmetry](https://github.com/traceloop/openllmetry) ![Stars](https://img.shields.io/github/stars/traceloop/openllmetry?style=social) - 基于 OpenTelemetry 的任意大语言模型提供商即插即用仪表化。
- [helicone](https://github.com/Helicone/helicone) ![Stars](https://img.shields.io/github/stars/Helicone/helicone?style=social) - 一行代码实现大语言模型可观测性监控和评估。
- [agenta](https://github.com/Agenta-AI/agenta) ![Stars](https://img.shields.io/github/stars/Agenta-AI/agenta?style=social) - LLMOps 平台：提示游乐场、管理、评估和可观测性。
- [openlit](https://github.com/openlit/openlit) ![Stars](https://img.shields.io/github/stars/openlit/openlit?style=social) - OpenTelemetry 原生的大语言模型可观测性、GPU 监控、护栏和评估。
- [weave](https://github.com/wandb/weave) ![Stars](https://img.shields.io/github/stars/wandb/weave?style=social) - Weights & Biases 的追踪、评估和监控工具包。
- [langsmith-sdk](https://github.com/langchain-ai/langsmith-sdk) ![Stars](https://img.shields.io/github/stars/langchain-ai/langsmith-sdk?style=social) - LangSmith 客户端 SDK，用于追踪、评估和调试。

</details>

### 评估

<details>
<summary><b>评估</b> — 大语言模型和代理的基准测试、测试和指标</summary>

- [promptfoo](https://github.com/promptfoo/promptfoo) ![Stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social) - 测试提示、代理和 RAG。AI 红队测试和漏洞扫描。
- [evals](https://github.com/openai/evals) ![Stars](https://img.shields.io/github/stars/openai/evals?style=social) - 评估大语言模型和大语言模型系统的框架及开源基准注册表。
- [deepeval](https://github.com/confident-ai/deepeval) ![Stars](https://img.shields.io/github/stars/confident-ai/deepeval?style=social) - 大语言模型评估框架 — 指标、数据集和集成。
- [ragas](https://github.com/explodinggradients/ragas) ![Stars](https://img.shields.io/github/stars/explodinggradients/ragas?style=social) - 评估 RAG 管道和大语言模型应用的框架。
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) ![Stars](https://img.shields.io/github/stars/EleutherAI/lm-evaluation-harness?style=social) - 语言模型少样本评估框架（200+ 任务）。
- [opencompass](https://github.com/open-compass/opencompass) ![Stars](https://img.shields.io/github/stars/open-compass/opencompass?style=social) - 大语言模型评估平台，支持 100+ 数据集跨主流模型。
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) ![Stars](https://img.shields.io/github/stars/SWE-bench/SWE-bench?style=social) - 大语言模型能否解决真实 GitHub issue？编码代理评估基准。
- [AgentBench](https://github.com/THUDM/AgentBench) ![Stars](https://img.shields.io/github/stars/THUDM/AgentBench?style=social) - 全面评估大语言模型作为代理的基准（ICLR'24）。
- [langwatch](https://github.com/langwatch/langwatch) ![Stars](https://img.shields.io/github/stars/langwatch/langwatch?style=social) - 大语言模型评估和 AI 代理测试平台。

</details>

### 幻觉检查

<details>
<summary><b>幻觉检查</b> — 事实核查、接地性和幻觉缓解</summary>

- [langextract](https://github.com/google/langextract) ![Stars](https://img.shields.io/github/stars/google/langextract?style=social) - 使用精确来源归因从非结构化文本中提取结构化信息。
- [git-mcp](https://github.com/idosal/git-mcp) ![Stars](https://img.shields.io/github/stars/idosal/git-mcp?style=social) - 终结代码幻觉。免费的 MCP 服务器，为 LLM 编码代理提供接地。
- [hallucination-leaderboard](https://github.com/vectara/hallucination-leaderboard) ![Stars](https://img.shields.io/github/stars/vectara/hallucination-leaderboard?style=social) - 比较大语言模型在文档摘要时产生幻觉的排行榜。
- [WikiChat](https://github.com/stanford-oval/WikiChat) ![Stars](https://img.shields.io/github/stars/stanford-oval/WikiChat?style=social) - 改进的 RAG，通过从语料库检索阻止大语言模型幻觉（斯坦福）。
- [uqlm](https://github.com/cvs-health/uqlm) ![Stars](https://img.shields.io/github/stars/cvs-health/uqlm?style=social) - 语言模型不确定性量化 — 基于不确定性的幻觉检测。
- [awesome-hallucination-detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) ![Stars](https://img.shields.io/github/stars/EdinburghNLP/awesome-hallucination-detection?style=social) - 大语言模型幻觉检测论文精选列表。
- [llm-hallucination-survey](https://github.com/HillZhang1999/llm-hallucination-survey) ![Stars](https://img.shields.io/github/stars/HillZhang1999/llm-hallucination-survey?style=social) - 大语言模型幻觉的阅读清单和综述。
- [dingo](https://github.com/MigoXLab/dingo) ![Stars](https://img.shields.io/github/stars/MigoXLab/dingo?style=social) - 覆盖幻觉检测的综合 AI 质量评估工具。
- [Woodpecker](https://github.com/VITA-MLLM/Woodpecker) ![Stars](https://img.shields.io/github/stars/VITA-MLLM/Woodpecker?style=social) - 多模态大语言模型的幻觉纠正。

</details>

### 成本监控

<details>
<summary><b>成本监控</b> — Token 使用追踪、费用管理和预算控制</summary>

- [langfuse](https://github.com/langfuse/langfuse) ![Stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social) - 内置成本追踪和指标的大语言模型工程平台。
- [openobserve](https://github.com/openobserve/openobserve) ![Stars](https://img.shields.io/github/stars/openobserve/openobserve?style=social) - 含大语言模型成本监控的可观测性平台（存储成本降低 140 倍）。
- [evidently](https://github.com/evidentlyai/evidently) ![Stars](https://img.shields.io/github/stars/evidentlyai/evidently?style=social) - ML 和大语言模型可观测性，含 100+ 评估和监控指标。
- [helicone](https://github.com/Helicone/helicone) ![Stars](https://img.shields.io/github/stars/Helicone/helicone?style=social) - 专注于成本追踪功能的大语言模型可观测性。
- [agentops](https://github.com/AgentOps-AI/agentops) ![Stars](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=social) - AI 代理监控和大语言模型成本追踪 Python SDK。
- [agenta](https://github.com/Agenta-AI/agenta) ![Stars](https://img.shields.io/github/stars/Agenta-AI/agenta?style=social) - 含大语言模型成本可观测性的 LLMOps 平台。
- [openlit](https://github.com/openlit/openlit) ![Stars](https://img.shields.io/github/stars/openlit/openlit?style=social) - OpenTelemetry 原生的大语言模型可观测性、GPU 监控和成本追踪。
- [langkit](https://github.com/whylabs/langkit) ![Stars](https://img.shields.io/github/stars/whylabs/langkit?style=social) - 监控大语言模型的工具包 — 文本质量、相关性指标、情感分析。

</details>

---

## 08. 安全层

### 沙箱化

<details>
<summary><b>沙箱化</b> — AI 代理安全的隔离执行环境</summary>

- [daytona](https://github.com/daytonaio/daytona) ![Stars](https://img.shields.io/github/stars/daytonaio/daytona?style=social) - 运行 AI 生成代码的安全弹性基础设施。
- [E2B](https://github.com/e2b-dev/E2B) ![Stars](https://img.shields.io/github/stars/e2b-dev/E2B?style=social) - 面向企业级 AI 代理的开源安全沙箱云环境。
- [microsandbox](https://github.com/superradcompany/microsandbox) ![Stars](https://img.shields.io/github/stars/superradcompany/microsandbox?style=social) - 安全、本地和可编程的 AI 代理沙箱。
- [sandbox-agent](https://github.com/rivet-dev/sandbox-agent) ![Stars](https://img.shields.io/github/stars/rivet-dev/sandbox-agent?style=social) - 通过 HTTP 在沙箱中运行编码代理。支持 Claude Code、Codex、OpenCode。
- [desktop](https://github.com/e2b-dev/desktop) ![Stars](https://img.shields.io/github/stars/e2b-dev/desktop?style=social) - E2B 桌面沙箱，支持安全的图形化计算机使用。
- [llm-sandbox](https://github.com/vndee/llm-sandbox) ![Stars](https://img.shields.io/github/stars/vndee/llm-sandbox?style=social) - 轻量级便携的大语言模型沙箱运行时 Python 库。
- [open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent) ![Stars](https://img.shields.io/github/stars/Chen-zexi/open-ptc-agent?style=social) - 基于 MCP 的沙箱化代码执行（可编程工具调用）。
- [the-agent-sandbox-taxonomy](https://github.com/kajogo777/the-agent-sandbox-taxonomy) ![Stars](https://img.shields.io/github/stars/kajogo777/the-agent-sandbox-taxonomy?style=social) - 评估 AI 代理沙箱的开放分类和评分框架。

</details>

### 权限控制

<details>
<summary><b>权限控制</b> — AI 代理的访问控制、授权和 RBAC</summary>

- [agentshield](https://github.com/affaan-m/agentshield) ![Stars](https://img.shields.io/github/stars/affaan-m/agentshield?style=social) - AI 代理安全扫描器。检测代理配置、MCP 服务器和工具权限中的漏洞。
- [crust](https://github.com/BakeLens/crust) ![Stars](https://img.shields.io/github/stars/BakeLens/crust?style=social) - 开源 AI 代理安全基础设施 — 拦截和阻止危险代理行为。
- [aport-agent-guardrails](https://github.com/aporthq/aport-agent-guardrails) ![Stars](https://img.shields.io/github/stars/aporthq/aport-agent-guardrails?style=social) - AI 代理的预操作授权护栏。支持 OpenAI、Claude Code、LangChain、CrewAI。
- [agent-guardrails](https://github.com/logi-cmd/agent-guardrails) ![Stars](https://img.shields.io/github/stars/logi-cmd/agent-guardrails?style=social) - 通过 MCP 实现 AI 编码代理的合并门禁和安全检查。

</details>

### 密钥管理

<details>
<summary><b>密钥管理</b> — API 密钥轮换、密钥管理和凭证安全</summary>

- [keypal](https://github.com/izadoesdev/keypal) ![Stars](https://img.shields.io/github/stars/izadoesdev/keypal?style=social) - TypeScript 库，支持哈希、过期和作用域的安全 API 密钥管理。
- [forge](https://github.com/TensorBlock/forge) ![Stars](https://img.shields.io/github/stars/TensorBlock/forge?style=social) - 自托管中间件，统一多 AI 提供商访问并含加密密钥管理。
- [voidllm](https://github.com/voidmind-io/voidllm) ![Stars](https://img.shields.io/github/stars/voidmind-io/voidllm?style=social) - 隐私优先的大语言模型代理，支持 API 密钥管理、负载均衡和限速。
- [cligate](https://github.com/codeking-ai/cligate) ![Stars](https://img.shields.io/github/stars/codeking-ai/cligate?style=social) - 多协议 AI 代理，支持账户池和 API 密钥管理（Claude Code、Codex CLI、Gemini CLI）。
- [agentfence](https://github.com/agentfence/agentfence) ![Stars](https://img.shields.io/github/stars/agentfence/agentfence?style=social) - 自动化 AI 代理安全测试 — 识别提示注入和密钥泄露。
- [llm-keypool](https://github.com/piyush-tyagi-13/llm-keypool) ![Stars](https://img.shields.io/github/stars/piyush-tyagi-13/llm-keypool?style=social) - 免费层大语言模型 API 密钥池，支持轮换、冷却处理和 OpenAI 兼容代理。

</details>

### 护栏

<details>
<summary><b>护栏</b> — 内容安全、输入输出过滤和行为约束</summary>

- [guardrails](https://github.com/guardrails-ai/guardrails) ![Stars](https://img.shields.io/github/stars/guardrails-ai/guardrails?style=social) - 为大语言模型添加护栏。
- [Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) ![Stars](https://img.shields.io/github/stars/NVIDIA-NeMo/Guardrails?style=social) - NVIDIA NeMo Guardrails — 大语言模型对话系统的可编程护栏。
- [PurpleLlama](https://github.com/meta-llama/PurpleLlama) ![Stars](https://img.shields.io/github/stars/meta-llama/PurpleLlama?style=social) - Meta 的工具，用于评估和改进大语言模型安全性。
- [llm-guard](https://github.com/protectai/llm-guard) ![Stars](https://img.shields.io/github/stars/protectai/llm-guard?style=social) - 大语言模型交互安全工具包（Protect AI）。
- [rebuff](https://github.com/protectai/rebuff) ![Stars](https://img.shields.io/github/stars/protectai/rebuff?style=social) - 大语言模型提示注入检测器。
- [modelscan](https://github.com/protectai/modelscan) ![Stars](https://img.shields.io/github/stars/protectai/modelscan?style=social) - 防御模型序列化攻击。

</details>

### 人工审批循环

<details>
<summary><b>人工审批循环</b> — 人工批准、监督和反馈机制</summary>

- [magentic-ui](https://github.com/microsoft/magentic-ui) ![Stars](https://img.shields.io/github/stars/microsoft/magentic-ui?style=social) - 实验性人工参与代理 UI，用于浏览器和文件系统任务。
- [Observal](https://github.com/BlazeUp-AI/Observal) ![Stars](https://img.shields.io/github/stars/BlazeUp-AI/Observal?style=social) - 专门为人工参与代理构建的可观测性和评估平台。
- [agent-inbox](https://github.com/langchain-ai/agent-inbox) ![Stars](https://img.shields.io/github/stars/langchain-ai/agent-inbox?style=social) - 与人工参与代理交互的收件箱式 UX — 审查和批准代理操作。
- [agent-approval-gate](https://github.com/renezander030/agent-approval-gate) ![Stars](https://img.shields.io/github/stars/renezander030/agent-approval-gate?style=social) - 生产审批门模式：草稿、验证、批准、分发、审计。

**注：** 内置 HITL 支持的主流代理框架包括 [AutoGen](https://github.com/microsoft/autogen)（HumanProxyAgent）、[CrewAI](https://github.com/crewAIInc/crewAI)（human_input 工具）和 [LangGraph](https://github.com/langchain-ai/langgraph)（interrupt_before/interrupt_after 检查点）。

</details>

---

## 贡献指南

欢迎贡献！请先阅读[贡献指南](CONTRIBUTING.md)。

## 许可证

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
