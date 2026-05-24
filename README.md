# Awesome AI Agent Framework [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

An architectural map of AI agent tooling across foundation models, agent brains, tools, workflows, multi-agent systems, infrastructure, observability, and security.

> **Disclaimer:** This list is a work in progress. Contributions are welcome!
> **Curation rule:** Each third-level topic lists up to 10 representative GitHub repositories. Fewer than 10 is fine when the category does not yet have enough strong, maintained projects.

## Contents

- [01. Foundation Layer](#01-foundation-layer)
  - [Large Language Models](#large-language-models)
  - [Prompt Engineering](#prompt-engineering)
  - [Context](#context)
- [02. Agent Brain](#02-agent-brain)
  - [Planning](#planning)
  - [Reasoning](#reasoning)
  - [Decision Engine](#decision-engine)
- [03. Tool Layer](#03-tool-layer)
- [04. Agent Workflows](#04-agent-workflows)
- [05. Multi-Agent Systems](#05-multi-agent-systems)
- [06. Infrastructure](#06-infrastructure)
- [07. Observability](#07-observability)
- [08. Security](#08-security)
- [Contributing](#contributing)

---

## 01. Foundation Layer

### Large Language Models

> **[Last reviewed: 2026-05-24]** Provider lineups change quickly. Each provider below lists five representative current or still-relevant models/product endpoints; check the official model page before relying on exact aliases, pricing, or availability.

#### Commercial / Cloud Providers

- **OpenAI**
  - [GPT-5.5](https://platform.openai.com/docs/models) - Flagship model for complex reasoning, coding, and professional work.
  - [GPT-5.4](https://platform.openai.com/docs/models) - More affordable frontier model for coding and professional work.
  - [GPT-5.4 mini](https://platform.openai.com/docs/models) - Strong mini model for coding, computer use, and subagents.
  - [GPT-5.4 nano](https://platform.openai.com/docs/models) - Lowest-latency, lowest-cost GPT-5.4-class model.
  - [GPT Image 2](https://platform.openai.com/docs/models) - State-of-the-art image generation and editing model.

- **Anthropic**
  - [Claude Opus 4.7](https://docs.anthropic.com/en/docs/about-claude/models/overview) - Most capable generally available Claude model for complex reasoning and agentic coding.
  - [Claude Opus 4.6](https://docs.anthropic.com/en/docs/about-claude/models/overview) - Previous Opus 4 generation for advanced multi-step work.
  - [Claude Sonnet 4.6](https://docs.anthropic.com/en/docs/about-claude/models/overview) - Best speed/intelligence balance in the current Claude lineup.
  - [Claude Sonnet 4.5](https://docs.anthropic.com/en/docs/about-claude/models/overview) - Strong Sonnet generation with extended thinking and broad cloud availability.
  - [Claude Haiku 4.5](https://docs.anthropic.com/en/docs/about-claude/models/overview) - Fastest current Claude model with near-frontier intelligence.

- **Google DeepMind**
  - [Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini) - Advanced intelligence for complex problem-solving, agentic, and coding tasks.
  - [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini) - Stable frontier-performance model for sustained agentic and coding workloads.
  - [Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini) - Frontier-class performance at a lower cost.
  - [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini) - Efficient Flash-Lite model for latency- and cost-sensitive workloads.
  - [Gemini 3.1 Flash Live](https://ai.google.dev/gemini-api/docs/models/gemini) - Low-latency Live API model for real-time dialogue and voice-first apps.

- **Mistral AI**
  - [Mistral Medium 3.5](https://docs.mistral.ai/getting-started/models/) - Frontier-class multimodal model for agentic and coding use cases.
  - [Mistral Large 3](https://docs.mistral.ai/getting-started/models/) - State-of-the-art open-weight general-purpose multimodal model.
  - [Mistral Small 4](https://docs.mistral.ai/getting-started/models/) - Efficient hybrid instruct, reasoning, and coding model.
  - [Magistral Medium 1.2](https://docs.mistral.ai/getting-started/models/) - Frontier multimodal reasoning model.
  - [Devstral 2](https://docs.mistral.ai/getting-started/models/) - Code-agent model for software engineering tasks.

- **Cohere**
  - [Command A+](https://docs.cohere.com/v2/docs/models/) - Latest MoE model for high-capability enterprise generation.
  - [Command A Reasoning](https://docs.cohere.com/v2/docs/models/) - Reasoning model for nuanced problem-solving and agent tasks.
  - [Command A](https://docs.cohere.com/docs/model-vault) - Strong general model across enterprise domains.
  - [Embed v4.0](https://docs.cohere.com/v2/docs/models/) - Multimodal embedding model for search and retrieval.
  - [Rerank v4.0 Pro](https://docs.cohere.com/v2/docs/models/) - High-quality reranking model for retrieval pipelines.

- **Amazon (Bedrock & Titan)**
  - [Nova Premier](https://aws.amazon.com/bedrock/nova/) - Most capable Amazon Nova model and teacher model for distillation.
  - [Nova Pro](https://aws.amazon.com/bedrock/nova/) - High-capability multimodal model.
  - [Nova Lite](https://aws.amazon.com/bedrock/nova/) - Cost-efficient model for high-volume workloads.
  - [Nova Micro](https://aws.amazon.com/bedrock/nova/) - Lowest-latency text-only model.
  - [Titan Text Premier](https://aws.amazon.com/bedrock/) - Enterprise-grade text generation.

- **xAI**
  - [Grok 4.3](https://docs.x.ai/developers/models) - Current flagship text model for agentic tool calling.
  - [Grok Build 0.1](https://docs.x.ai/developers/models) - Coding-focused endpoint for build workflows.
  - [Grok Voice API](https://docs.x.ai/developers/models) - Realtime speech-to-text, text-to-speech, and voice-agent capability.
  - [Grok Imagine Image API](https://docs.x.ai/developers/models) - Image generation and editing endpoint.
  - [Grok Imagine Video API](https://docs.x.ai/developers/models) - Video generation and editing endpoint.

- **AI21 Labs**
  - [Jamba Large 1.7](https://docs.ai21.com/docs/jamba-foundation-models) - Most powerful Jamba model for enterprise-scale complex tasks.
  - [Jamba Mini 2](https://docs.ai21.com/docs/jamba-foundation-models) - 12B-active efficient model for enterprise workflows.
  - [Jamba2 Mini](https://docs.ai21.com/docs/jamba-foundation-models) - Efficient and steerable model line for core enterprise tasks.
  - [Jamba2 3B](https://docs.ai21.com/docs/jamba-foundation-models) - Compact model for on-device and agentic systems.
  - [AI21 Maestro](https://docs.ai21.com/docs/jamba-foundation-models) - Agentic orchestration layer built around AI21 foundation models.

- **Reka**
  - [Reka Flash 3](https://reka.ai/news/introducing-reka-flash) - Open reasoning-preview model in the Flash family.
  - [Reka Core](https://reka.ai/) - Largest and most capable multimodal model in the Reka family.
  - [Reka Flash](https://docs.reka.ai/chat/models) - Fast multimodal production model.
  - [Reka Edge](https://reka.ai/) - Lightweight multimodal model for edge deployment.
  - [Reka Core 20240501](https://v0.docs.reka.ai/guides/005-listing-models.html) - Versioned Core API model for stable deployments.

- **Writer**
  - [Palmyra X5](https://writer.com/llms/) - Advanced long-context model for enterprise agents.
  - [Palmyra X4](https://dev.writer.com/home/models) - Previous-generation enterprise general model.
  - [Palmyra X 004](https://dev.writer.com/home/models) - Enterprise model for tool use and knowledge workflows.
  - [Palmyra Med](https://dev.writer.com/home/models) - Healthcare-specialized model line.
  - [Palmyra Fin](https://dev.writer.com/home/models) - Finance-specialized model line.

- **Perplexity**
  - [Sonar](https://docs.perplexity.ai/getting-started/models) - Lightweight grounded search model.
  - [Sonar Pro](https://docs.perplexity.ai/getting-started/models) - Advanced grounded search model for complex queries.
  - [Sonar Reasoning Pro](https://docs.perplexity.ai/docs/sonar/models/sonar-reasoning-pro) - Advanced multi-step reasoning model with retrieval.
  - [Sonar Deep Research](https://docs.perplexity.ai/getting-started/models) - Deep-research-oriented model for longer investigations.
  - [Sonar API](https://docs.perplexity.ai/getting-started/models) - Programmatic search-answering endpoint family.

- **Inflection AI**
  - [Inflection 3.0 Enterprise](https://inflection.ai/enterprise) - Enterprise AI system tuned for organization-specific workflows.
  - [Inflection 3.0](https://inflection.ai/enterprise) - Foundation model behind Inflection's enterprise offering.
  - [Pi](https://inflection.ai/) - Consumer conversational assistant powered by Inflection models.
  - [Inflection-2.5](https://inflection.ai/) - Previous high-capability model generation for Pi.
  - [Inflection Enterprise Custom Models](https://inflection.ai/enterprise) - Fine-tuned private deployments for business processes.

#### Open-Source / Open-Weight Providers

- **Meta**
  - [Llama 4 Maverick](https://llama.meta.com/) - 400B MoE open-weight multimodal model (17B-128E).
  - [Llama 4 Scout](https://llama.meta.com/) - 109B MoE model with 10M token context (17B-16E).
  - [Llama 3.1 405B](https://llama.meta.com/) - Largest dense open-weight model.
  - [Llama 3.3 70B](https://llama.meta.com/) - Improved 70B parameter model.
  - [Llama 3.2 Vision](https://llama.meta.com/) - Open-weight multimodal models (11B/90B).

- **DeepSeek**
  - [DeepSeek-V3.2](https://github.com/deepseek-ai/DeepSeek-V3) - Agent-oriented MoE model with integrated thinking and tool use.
  - [DeepSeek-V3.2-Speciale](https://github.com/deepseek-ai/DeepSeek-V3) - Reasoning-specialized V3.2 variant for math and coding.
  - [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) - Open-weight reasoning model that catalyzed the 2025 reasoning-model wave.
  - [DeepSeek-Prover-V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2) - Theorem proving specialized model.
  - [Janus-Pro](https://github.com/deepseek-ai/DeepSeek-VL2) - Multimodal understanding and generation model family.

- **Qwen Team (Alibaba Open-Weight)**
  - [Qwen3.6-27B](https://github.com/QwenLM/Qwen3) - Dense open-weight model with strong agentic coding performance.
  - [Qwen3-Coder-Next](https://github.com/QwenLM/Qwen3-Coder) - Coding-agent model specialized for software engineering workflows.
  - [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) - Vision-language family for long-context multimodal reasoning.
  - [Qwen3-VL-Embedding / Reranker](https://github.com/QwenLM/Qwen3-VL) - Multimodal retrieval and ranking models.
  - [Qwen3-235B-A22B](https://github.com/QwenLM/Qwen3) - Large MoE open-weight model for hybrid thinking.

- **Microsoft**
  - [Phi-4-reasoning-vision-15B](https://github.com/microsoft/Phi-4-reasoning-vision-15B) - Open-weight multimodal reasoning model.
  - [Phi-4-reasoning-plus](https://azure.microsoft.com/en-us/products/phi) - Stronger Phi-4 reasoning variant for math and logic.
  - [Phi-4-reasoning](https://azure.microsoft.com/en-us/products/phi) - Compact reasoning model in the Phi-4 family.
  - [Phi-4-mini-flash-reasoning](https://azure.microsoft.com/en-us/products/phi) - Low-latency hybrid reasoning model.
  - [Phi-4-multimodal](https://azure.microsoft.com/en-us/products/phi) - Compact multimodal Phi model for speech, vision, and text.

- **NVIDIA**
  - [Nemotron 3 Ultra](https://research.nvidia.com/labs/nemotron/Nemotron-3/) - Largest Nemotron 3 model for complex agentic reasoning.
  - [Nemotron 3 Super](https://research.nvidia.com/labs/nemotron/Nemotron-3-Super/) - 120B-parameter open MoE model for multi-agent systems.
  - [Nemotron 3 Nano](https://research.nvidia.com/labs/nemotron/Nemotron-3/) - Efficient open model for local and edge agent workloads.
  - [Nemotron 3 Nano Omni](https://build.nvidia.com/) - Compact multimodal Nemotron variant.
  - [Llama-3.1-Nemotron-Ultra 253B](https://build.nvidia.com/) - Fine-tuned reasoning model from the earlier Nemotron line.

- **Databricks**
  - [DBRX Instruct](https://www.databricks.com/) - Open-weight 132B MoE instruction-following model.
  - [DBRX Base](https://www.databricks.com/) - Open-weight foundation MoE model.
  - [MPT-30B](https://www.databricks.com/) - MosaicML open foundation model lineage acquired by Databricks.
  - [MPT-7B](https://www.databricks.com/) - Earlier MosaicML open model for efficient fine-tuning.
  - [Dolly v2](https://www.databricks.com/) - Instruction-following model that helped popularize open commercial-use instruction data.

- **Snowflake**
  - [Arctic](https://docs.snowflake.com/) - Open-weight 480B MoE for enterprise tasks.
  - [Arctic Embed Large](https://docs.snowflake.com/) - High-accuracy open text embedding model.
  - [Arctic Embed Medium](https://docs.snowflake.com/) - Balanced embedding model for retrieval systems.
  - [Arctic Embed Small](https://docs.snowflake.com/) - Compact embedding model for cost-sensitive search.
  - [Arctic Extract](https://docs.snowflake.com/) - Document extraction model for structured business data.

- **Allen AI (AI2)**
  - [OLMo 3 Think 32B](https://allenai.org/) - Fully open thinking model with open training artifacts.
  - [OLMo 2 32B](https://allenai.org/) - Fully open foundation model with data, code, and checkpoints.
  - [Tulu 3](https://allenai.org/) - Open post-training and instruction-following model family.
  - [OLMoE](https://allenai.org/) - Open mixture-of-experts language model.
  - [Molmo](https://allenai.org/) - Open multimodal model family for vision-language tasks.

- **Stability AI**
  - [Stable LM 2 12B](https://stability.ai/core-models) - Open-weight language model.
  - [Stable LM 2 1.6B](https://stability.ai/core-models) - Compact multilingual language model.
  - [Stable Code 3B](https://stability.ai/core-models) - Compact code foundation model.
  - [Stable Code Instruct 3B](https://stability.ai/core-models) - Instruction-tuned code model.
  - [Stable Audio 3](https://stability.ai/research/stable-audio-3) - Current open audio model family for generative media workflows.

- **Hugging Face (Community)**
  - [SmolLM3](https://huggingface.co/HuggingFaceTB) - Compact open language model family for efficient deployment.
  - [SmolVLM](https://huggingface.co/HuggingFaceTB) - Compact vision-language model family.
  - [Zephyr](https://huggingface.co/HuggingFaceH4) - Fine-tuned open chat model lineage.
  - [Idefics](https://huggingface.co/HuggingFaceM4) - Open multimodal model family from Hugging Face.
  - [StarCoder2](https://huggingface.co/bigcode) - Open code model family from the BigCode community.

- **Cohere For AI (Research)**
  - [Command A+](https://cohere.com/research) - Open enterprise model with multimodal reasoning and agentic capabilities.
  - [Command A](https://cohere.com/research) - Enterprise-ready open model for generation and tool use.
  - [Command R7B](https://cohere.com/research) - Compact open model optimized for retrieval-augmented generation.
  - [Aya Expanse](https://cohere.com/research) - Multilingual open model family.
  - [Aya 23](https://cohere.com/research) - Open-weight multilingual model family covering 23 languages.

#### Chinese Ecosystem

- **Alibaba Cloud (通义千问)**
  - [Qwen3-Max](https://tongyi.aliyun.com/) - Flagship commercial Qwen model for complex reasoning and enterprise tasks.
  - [Qwen3-Plus](https://tongyi.aliyun.com/) - Balanced commercial model for production workloads.
  - [Qwen3-Turbo](https://tongyi.aliyun.com/) - Fast, cost-efficient model for high-throughput applications.
  - [Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) - Code-specialized Qwen model for agentic software engineering.
  - [Qwen3-VL-Max](https://github.com/QwenLM/Qwen3-VL) - Commercial multimodal vision-language model.

- **Baidu (文心一言 / ERNIE)**
  - [ERNIE 5.0](https://yiyan.baidu.com/) - Latest flagship ERNIE generation for multimodal reasoning.
  - [ERNIE X1](https://yiyan.baidu.com/) - Deep-thinking reasoning model.
  - [ERNIE 4.5](https://yiyan.baidu.com/) - Strong multimodal foundation model for enterprise use.
  - [ERNIE Speed](https://yiyan.baidu.com/) - Fast inference model for high-volume tasks.
  - [ERNIE Lite](https://yiyan.baidu.com/) - Lightweight model for cost-sensitive production.

- **Zhipu AI (智谱清言)**
  - [GLM-4.6](https://bigmodel.cn/) - Current flagship general-purpose model.
  - [GLM-4.5V](https://bigmodel.cn/) - Vision-language model for multimodal understanding.
  - [GLM-Z1](https://bigmodel.cn/) - Reasoning-focused GLM model family.
  - [GLM-4-Flash](https://bigmodel.cn/) - Fast, low-cost inference model.
  - [CogVideoX](https://bigmodel.cn/) - Open video generation model.

- **Moonshot AI (Kimi / 月之暗面)**
  - [Kimi K2 Thinking](https://kimi.moonshot.cn/) - Long-horizon reasoning model for complex agentic work.
  - [Kimi K2](https://kimi.moonshot.cn/) - Flagship MoE model with strong tool-use and long-context capability.
  - [Kimi Linear](https://kimi.moonshot.cn/) - Efficient long-context model architecture from Moonshot AI.
  - [moonshot-v1-128k](https://platform.moonshot.cn/) - Long-context API model for document-heavy tasks.
  - [moonshot-v1-32k](https://platform.moonshot.cn/) - Balanced long-context API model.

- **ByteDance (豆包 / Doubao / Seed)**
  - [Seed1.6](https://github.com/ByteDance-Seed) - Latest Seed foundation model line from ByteDance.
  - [Seed1.5-VL](https://github.com/ByteDance-Seed/Seed1.5-VL) - Flagship vision-language MoE model.
  - [Seed-Coder](https://github.com/ByteDance-Seed) - Coding-specialized model family.
  - [Doubao-Pro](https://team.doubao.com/) - Flagship commercial model.
  - [Doubao-Lite](https://team.doubao.com/) - Lightweight fast commercial model.

- **Tencent (腾讯混元 / Hunyuan)**
  - [Hunyuan TurboS](https://github.com/Tencent/Hunyuan-TurboS) - Flagship fast-thinking MoE model, Hybrid-Mamba-Transformer architecture.
  - [Hunyuan T1](https://github.com/Tencent/llm.hunyuan.T1) - RL-driven reasoning model.
  - [Hunyuan-Large](https://hunyuan.tencent.com/) - Open-weight 389B MoE model.
  - [Hunyuan-Pro](https://hunyuan.tencent.com/) - Commercial API flagship.
  - [Hunyuan-Video](https://hunyuan.tencent.com/) - Open video generation model.

- **MiniMax (海螺AI)**
  - [MiniMax-M2](https://www.minimaxi.com/) - Open-weight agentic model for coding and tool use.
  - [MiniMax-Text-01](https://www.minimaxi.com/) - Open-weight 456B MoE long-context text model.
  - [MiniMax-VL-01](https://www.minimaxi.com/) - Vision-language model.
  - [Video-01](https://www.minimaxi.com/) - Video generation model.
  - [Speech-01](https://www.minimaxi.com/) - Text-to-speech model.

- **Baichuan AI (百川智能)**
  - [Baichuan-M3](https://www.baichuan-ai.com/) - Medical-specialized model from Baichuan.
  - [Baichuan 4](https://www.baichuan-ai.com/) - Flagship general model with reasoning and coding capability.
  - [Baichuan 3](https://www.baichuan-ai.com/) - Previous-generation general-purpose model.
  - [Baichuan 2 13B](https://www.baichuan-ai.com/) - Open-weight bilingual model.
  - [Baichuan 2 7B](https://www.baichuan-ai.com/) - Smaller open-weight bilingual model.

- **01.AI (零一万物)**
  - [Yi-Lightning](https://www.01.ai/) - Ultra-fast, cost-efficient commercial model.
  - [Yi-Large](https://www.01.ai/) - Flagship general-purpose model line.
  - [Yi-Vision](https://www.01.ai/) - Multimodal vision-language model.
  - [Yi-34B](https://www.01.ai/) - Open-weight bilingual model.
  - [Yi-9B](https://www.01.ai/) - Smaller open-weight bilingual model.

- **iFlytek (科大讯飞 / Spark)**
  - [Spark X1](https://xinghuo.xfyun.cn/) - Deep reasoning model in the Spark family.
  - [Spark 4.0 Ultra](https://xinghuo.xfyun.cn/) - Flagship general model with strong Chinese capabilities.
  - [Spark Max](https://xinghuo.xfyun.cn/) - High-capability production model.
  - [Spark Pro](https://xinghuo.xfyun.cn/) - Balanced enterprise model.
  - [Spark Lite](https://xinghuo.xfyun.cn/) - Lightweight model for cost-sensitive workloads.

- **SenseTime (商汤日日新 / SenseNova)**
  - [SenseNova 6.0](https://sensenova.sensetime.com/) - Latest multimodal model generation from SenseTime.
  - [SenseNova 5.5](https://sensenova.sensetime.com/) - Flagship multimodal model.
  - [SenseChat](https://sensenova.sensetime.com/) - Conversational model for enterprise assistants.
  - [SenseMirage](https://sensenova.sensetime.com/) - Image generation model family.
  - [SenseTime Vimi](https://sensenova.sensetime.com/) - Video and digital-human generation model family.

#### On-Device / Edge

- **Apple** - [AFM (Apple Foundation Model)](https://machinelearning.apple.com/) - On-device and server models powering Apple Intelligence.
- **Samsung** - [Samsung Gauss](https://research.samsung.com/) - On-device and server LLMs for Galaxy ecosystem.

#### Inference Platforms (Hosted Open Models)

- [Together AI](https://together.ai/) - Serverless inference for 200+ open-source models.
- [Fireworks AI](https://fireworks.ai/) - Fast, cost-effective serving for open LLMs.
- [Groq](https://groq.com/) - LPU-based ultra-fast inference for open models.
- [Cerebras](https://cerebras.ai/) - Wafer-scale inference for open models.

### Prompt Engineering

<details>
<summary><b>System Prompts</b> — Collections and tools for LLM system prompts</summary>

- [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) ![Stars](https://img.shields.io/github/stars/x1xhlol/system-prompts-and-models-of-ai-tools?style=social) `Framework` - Full system prompts extracted from Augment Code, Claude Code, Cursor, Devin, Manus, Perplexity, Windsurf, v0, etc.
- [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) ![Stars](https://img.shields.io/github/stars/asgeirtj/system_prompts_leaks?style=social) `Framework` - Extracted system prompts from ChatGPT, Claude, Gemini, Grok, Copilot, Perplexity, and more.
- [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) ![Stars](https://img.shields.io/github/stars/elder-plinius/CL4R1T4S?style=social) `Framework` - Leaked system prompts for transparency — ChatGPT, Claude, Gemini, Grok, Cursor, Lovable, Replit.
- [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) ![Stars](https://img.shields.io/github/stars/jujumilk3/leaked-system-prompts?style=social) `Framework` - Collection of leaked system prompts from various LLM products.
- [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt) ![Stars](https://img.shields.io/github/stars/LouisShark/chatgpt_system_prompt?style=social) `Framework` - GPT system prompts with prompt injection and leaking techniques.
- [claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) ![Stars](https://img.shields.io/github/stars/Piebald-AI/claude-code-system-prompts?style=social) `Framework` `Infra` - All parts of Claude Code's system prompt: 27 builtin tools, sub-agent prompts, utility prompts.
- [awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts) ![Stars](https://img.shields.io/github/stars/dontriskit/awesome-ai-system-prompts?style=social) `Framework` `Research` - Curated system prompts for ChatGPT, Claude, Perplexity, Manus, Claude Code, Lovable, v0, Grok.
- [TheBigPromptLibrary](https://github.com/0xeb/TheBigPromptLibrary) ![Stars](https://img.shields.io/github/stars/0xeb/TheBigPromptLibrary?style=social) `Framework` - Large collection of prompts, system prompts, and LLM instructions.
- [tweakcc](https://github.com/Piebald-AI/tweakcc) ![Stars](https://img.shields.io/github/stars/Piebald-AI/tweakcc?style=social) `Framework` `Infra` - Customize Claude Code's system prompts, toolsets, and themes.
- [awesome-system-prompts](https://github.com/langgptai/awesome-system-prompts) ![Stars](https://img.shields.io/github/stars/langgptai/awesome-system-prompts?style=social) `Framework` `Research` - System prompts of DeepSeek, ChatGPT, Gemini, Grok, Qwen.

</details>

<details>
<summary><b>Few-Shot / In-Context Learning</b> — Learning from demonstrations</summary>

- [Otter](https://github.com/EvolvingLMMs-Lab/Otter) ![Stars](https://img.shields.io/github/stars/EvolvingLMMs-Lab/Otter?style=social) `Framework` `Example` - Multi-modal model with improved instruction-following and in-context learning.
- [prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning) ![Stars](https://img.shields.io/github/stars/EgoAlpha/prompt-in-context-learning?style=social) `Framework` `Example` - Awesome resources for in-context learning and prompt engineering.
- [ICL_PaperList](https://github.com/dqxiu/ICL_PaperList) ![Stars](https://img.shields.io/github/stars/dqxiu/ICL_PaperList?style=social) `Framework` `Example` `Research` `Infra` - Curated research papers on in-context learning.
- [OpenICL](https://github.com/Shark-NLP/OpenICL) ![Stars](https://img.shields.io/github/stars/Shark-NLP/OpenICL?style=social) `Framework` `Example` `Research` `Infra` - Open-source framework for in-context learning research and prototyping.
- [DINOv](https://github.com/UX-Decoder/DINOv) ![Stars](https://img.shields.io/github/stars/UX-Decoder/DINOv?style=social) `Official` `Framework` `Example` `Research` - Visual in-context learning (CVPR 2024).
- [t-few](https://github.com/r-three/t-few) ![Stars](https://img.shields.io/github/stars/r-three/t-few?style=social) `Framework` `Example` - Few-shot parameter-efficient fine-tuning vs in-context learning.
- [xmc.dspy](https://github.com/KarelDO/xmc.dspy) ![Stars](https://img.shields.io/github/stars/KarelDO/xmc.dspy?style=social) `Framework` `Example` `Research` - In-context learning for extreme multi-label classification.
- [prompt-lib](https://github.com/reasoning-machines/prompt-lib) ![Stars](https://img.shields.io/github/stars/reasoning-machines/prompt-lib?style=social) `Framework` `Example` `Research` - Utilities for few-shot prompting experiments on LLMs.
- [TextualExplInContext](https://github.com/xiye17/TextualExplInContext) ![Stars](https://img.shields.io/github/stars/xiye17/TextualExplInContext?style=social) `Framework` `Example` `Research` - Unreliability of explanations in few-shot prompting (NeurIPS 2022).
- [bullet](https://github.com/rafaelpierre/bullet) ![Stars](https://img.shields.io/github/stars/rafaelpierre/bullet?style=social) `Framework` `Example` - Zero-shot / few-shot LLM-based text classification framework.

</details>

<details>
<summary><b>Chain-of-Thought / Reasoning</b> — Step-by-step reasoning techniques</summary>

- [Awesome-LLM-Strawberry](https://github.com/hijkzzz/Awesome-LLM-Strawberry) ![Stars](https://img.shields.io/github/stars/hijkzzz/Awesome-LLM-Strawberry?style=social) `Framework` `Research` - Papers and projects on OpenAI o1 and reasoning techniques.
- [tree-of-thought-llm](https://github.com/princeton-nlp/tree-of-thought-llm) ![Stars](https://img.shields.io/github/stars/princeton-nlp/tree-of-thought-llm?style=social) `Framework` `Research` `Infra` - Tree of Thoughts: Deliberate Problem Solving with LLMs (NeurIPS 2023).
- [deepreasoning](https://github.com/winfunc/deepreasoning) ![Stars](https://img.shields.io/github/stars/winfunc/deepreasoning?style=social) `Framework` `Research` `Infra` - DeepSeek R1 CoT reasoning traces integrated with Claude models.
- [tree-of-thoughts](https://github.com/kyegomez/tree-of-thoughts) ![Stars](https://img.shields.io/github/stars/kyegomez/tree-of-thoughts?style=social) `Framework` `Research` - Plug-and-play Tree of Thoughts implementation.
- [reasoning-from-scratch](https://github.com/rasbt/reasoning-from-scratch) ![Stars](https://img.shields.io/github/stars/rasbt/reasoning-from-scratch?style=social) `Framework` `Example` `Research` - Implement a reasoning LLM in PyTorch from scratch.
- [mm-cot](https://github.com/amazon-science/mm-cot) ![Stars](https://img.shields.io/github/stars/amazon-science/mm-cot?style=social) `Official` `Framework` `Research` - Multimodal Chain-of-Thought Reasoning in Language Models.
- [Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) ![Stars](https://img.shields.io/github/stars/atfortes/Awesome-LLM-Reasoning?style=social) `Framework` `Research` - From CoT prompting to o1 and DeepSeek-R1 — curated reasoning resource list.
- [chain-of-thought-hub](https://github.com/FranxYao/chain-of-thought-hub) ![Stars](https://img.shields.io/github/stars/FranxYao/chain-of-thought-hub?style=social) `Framework` `Research` - Benchmarking LLMs' complex reasoning with CoT prompting.
- [Chain-of-ThoughtsPapers](https://github.com/Timothyxxx/Chain-of-ThoughtsPapers) ![Stars](https://img.shields.io/github/stars/Timothyxxx/Chain-of-ThoughtsPapers?style=social) `Framework` `Research` `Infra` `Archived Classic` - Paper collection tracing the CoT reasoning trend.
- [auto-cot](https://github.com/amazon-science/auto-cot) ![Stars](https://img.shields.io/github/stars/amazon-science/auto-cot?style=social) `Official` `Framework` `Research` - Automatic Chain-of-Thought Prompting in LLMs.

</details>

<details>
<summary><b>Structured Output</b> — JSON, schemas, and constrained generation</summary>

- [guidance](https://github.com/guidance-ai/guidance) ![Stars](https://img.shields.io/github/stars/guidance-ai/guidance?style=social) `Framework` - Constraint-based generation with templating for controlling LLMs.
- [pydantic-ai](https://github.com/pydantic/pydantic-ai) ![Stars](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=social) `Official` `Framework` - AI Agent Framework — structured output via Pydantic type annotations.
- [outlines](https://github.com/dottxt-ai/outlines) ![Stars](https://img.shields.io/github/stars/dottxt-ai/outlines?style=social) `Framework` - Structured generation via token-level constrained decoding (regex, JSON Schema, CFG).
- [instructor](https://github.com/567-labs/instructor) ![Stars](https://img.shields.io/github/stars/567-labs/instructor?style=social) `Framework` - Patches OpenAI/Anthropic clients to return Pydantic models.
- [TypeChat](https://github.com/microsoft/TypeChat) ![Stars](https://img.shields.io/github/stars/microsoft/TypeChat?style=social) `Official` `Framework` - Maps natural language intent to typed JSON using TypeScript types.
- [guardrails](https://github.com/guardrails-ai/guardrails) ![Stars](https://img.shields.io/github/stars/guardrails-ai/guardrails?style=social) `Framework` `Infra` - Input/output validation, schema enforcement, and re-asking for LLMs.
- [jsonformer](https://github.com/1rgs/jsonformer) ![Stars](https://img.shields.io/github/stars/1rgs/jsonformer?style=social) `Framework` - Bulletproof structured JSON generation via constrained decoding.
- [lmql](https://github.com/eth-sri/lmql) ![Stars](https://img.shields.io/github/stars/eth-sri/lmql?style=social) `Framework` - Declarative constraint language for guided LLM programming.
- [lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer) ![Stars](https://img.shields.io/github/stars/noamgat/lm-format-enforcer?style=social) `Framework` - Enforce JSON Schema, Regex, etc. at generation time.
- [xgrammar](https://github.com/mlc-ai/xgrammar) ![Stars](https://img.shields.io/github/stars/mlc-ai/xgrammar?style=social) `Framework` - Fast grammar-based constrained decoding for structured generation.

</details>

### Context

<details>
<summary><b>Memory</b> — Long-term and short-term memory for AI agents</summary>

- [mempalace](https://github.com/MemPalace/mempalace) ![Stars](https://img.shields.io/github/stars/MemPalace/mempalace?style=social) `Framework` `Research` - Best-benchmarked open-source AI memory system.
- [mem0](https://github.com/mem0ai/mem0) ![Stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social) `Official` `Framework` - Memory layer for AI agents.
- [letta](https://github.com/letta-ai/letta) ![Stars](https://img.shields.io/github/stars/letta-ai/letta?style=social) `Official` `Framework` - Build stateful LLM agents with MemGPT.
- [hindsight](https://github.com/vectorize-io/hindsight) ![Stars](https://img.shields.io/github/stars/vectorize-io/hindsight?style=social) `Framework` - Agent memory that learns.
- [TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) ![Stars](https://img.shields.io/github/stars/Tencent/TencentDB-Agent-Memory?style=social) `Official` `Framework` `Infra` - Fully local 4-tier progressive memory pipeline, zero external API dependencies.
- [A-MEM](https://github.com/agiresearch/A-MEM) ![Stars](https://img.shields.io/github/stars/agiresearch/A-MEM?style=social) `Framework` - Agentic memory for LLM agents.
- [Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory) ![Stars](https://img.shields.io/github/stars/IAAR-Shanghai/Awesome-AI-Memory?style=social) `Framework` `Research` `Infra` - Curated knowledge base on AI memory — research, frameworks, benchmarks.
- [general-agentic-memory](https://github.com/VectorSpaceLab/general-agentic-memory) ![Stars](https://img.shields.io/github/stars/VectorSpaceLab/general-agentic-memory?style=social) `Framework` `Research` `Infra` - General memory system for agents, powered by deep-research.
- [mcp-mem0](https://github.com/coleam00/mcp-mem0) ![Stars](https://img.shields.io/github/stars/coleam00/mcp-mem0?style=social) `Framework` `Example` `Infra` - MCP server for long-term agent memory with Mem0 integration.
- [memoir](https://github.com/zhangfengcdt/memoir) ![Stars](https://img.shields.io/github/stars/zhangfengcdt/memoir?style=social) `Framework` - Hierarchical agent memory with Git-like version control.

</details>

<details>
<summary><b>RAG</b> — Retrieval-Augmented Generation frameworks and tools</summary>

- [ragflow](https://github.com/infiniflow/ragflow) ![Stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social) `Official` `Framework` `Research` `Infra` - Leading open-source RAG engine with agent capabilities.
- [LightRAG](https://github.com/HKUDS/LightRAG) ![Stars](https://img.shields.io/github/stars/HKUDS/LightRAG?style=social) `Framework` `Research` - Simple and fast retrieval-augmented generation (EMNLP 2025).
- [graphrag](https://github.com/microsoft/graphrag) ![Stars](https://img.shields.io/github/stars/microsoft/graphrag?style=social) `Official` `Framework` `Research` - Modular graph-based RAG system from Microsoft.
- [RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) ![Stars](https://img.shields.io/github/stars/NirDiamant/RAG_Techniques?style=social) `Official` `Framework` `Example` `Research` `Infra` - Advanced RAG techniques with detailed notebook tutorials.
- [memvid](https://github.com/memvid/memvid) ![Stars](https://img.shields.io/github/stars/memvid/memvid?style=social) `Framework` `Research` `Infra` - Serverless single-file replacement for complex RAG pipelines.
- [llmware](https://github.com/llmware-ai/llmware) ![Stars](https://img.shields.io/github/stars/llmware-ai/llmware?style=social) `Framework` `Research` - Unified enterprise RAG framework with small specialized models.
- [orama](https://github.com/oramasearch/orama) ![Stars](https://img.shields.io/github/stars/oramasearch/orama?style=social) `Framework` `Research` `Infra` - Complete search engine with full-text, vector, and hybrid search.
- [R2R](https://github.com/SciPhi-AI/R2R) ![Stars](https://img.shields.io/github/stars/SciPhi-AI/R2R?style=social) `Framework` `Research` `Infra` - Production-ready agentic RAG with RESTful API.
- [Verba](https://github.com/weaviate/Verba) ![Stars](https://img.shields.io/github/stars/weaviate/Verba?style=social) `Official` `Framework` `Research` - RAG chatbot powered by Weaviate.
- [azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo) ![Stars](https://img.shields.io/github/stars/Azure-Samples/azure-search-openai-demo?style=social) `Official` `Framework` `Example` `Research` `Infra` - Reference RAG app using Azure AI Search + OpenAI.

</details>

<details>
<summary><b>Vector Database</b> — Storage and search for embeddings</summary>

- [milvus](https://github.com/milvus-io/milvus) ![Stars](https://img.shields.io/github/stars/milvus-io/milvus?style=social) `Official` `Framework` `Infra` - High-performance cloud-native vector database for ANN search.
- [faiss](https://github.com/facebookresearch/faiss) ![Stars](https://img.shields.io/github/stars/facebookresearch/faiss?style=social) `Official` `Framework` `Infra` - Library for efficient similarity search and clustering of dense vectors.
- [qdrant](https://github.com/qdrant/qdrant) ![Stars](https://img.shields.io/github/stars/qdrant/qdrant?style=social) `Official` `Framework` `Infra` - High-performance vector database and search engine for next-gen AI.
- [chroma](https://github.com/chroma-core/chroma) ![Stars](https://img.shields.io/github/stars/chroma-core/chroma?style=social) `Official` `Framework` `Infra` - Open-source embedding database for AI applications.
- [pgvector](https://github.com/pgvector/pgvector) ![Stars](https://img.shields.io/github/stars/pgvector/pgvector?style=social) `Framework` `Infra` - Open-source vector similarity search extension for Postgres.
- [weaviate](https://github.com/weaviate/weaviate) ![Stars](https://img.shields.io/github/stars/weaviate/weaviate?style=social) `Official` `Framework` `Research` `Infra` - Open-source vector database with structured filtering.
- [lancedb](https://github.com/lancedb/lancedb) ![Stars](https://img.shields.io/github/stars/lancedb/lancedb?style=social) `Official` `Framework` `Research` `Infra` - Developer-friendly embedded retrieval library for multimodal AI.
- [RediSearch](https://github.com/RediSearch/RediSearch) ![Stars](https://img.shields.io/github/stars/RediSearch/RediSearch?style=social) `Official` `Framework` `Infra` - Query and indexing engine for Redis with vector similarity search.
- [helix-db](https://github.com/HelixDB/helix-db) ![Stars](https://img.shields.io/github/stars/HelixDB/helix-db?style=social) `Framework` `Infra` - Open-source graph-vector database built in Rust.
- [cozo](https://github.com/cozodb/cozo) ![Stars](https://img.shields.io/github/stars/cozodb/cozo?style=social) `Framework` `Infra` - Transactional relational-graph-vector database using Datalog.

</details>

<details>
<summary><b>Knowledge Graph</b> — Structured knowledge for AI agents</summary>

- [graphify](https://github.com/safishamsi/graphify) ![Stars](https://img.shields.io/github/stars/safishamsi/graphify?style=social) `Framework` `Research` `Infra` - Turn any folder into a queryable knowledge graph for AI coding assistants.
- [GitNexus](https://github.com/abhigyanpatwari/GitNexus) ![Stars](https://img.shields.io/github/stars/abhigyanpatwari/GitNexus?style=social) `Framework` `Infra` - Zero-server client-side knowledge graph with built-in Graph RAG agent.
- [graphiti](https://github.com/getzep/graphiti) ![Stars](https://img.shields.io/github/stars/getzep/graphiti?style=social) `Official` `Framework` `Infra` - Build real-time knowledge graphs for AI agents.
- [Understand-Anything](https://github.com/Lum1104/Understand-Anything) ![Stars](https://img.shields.io/github/stars/Lum1104/Understand-Anything?style=social) `Framework` `Infra` - Turn any code into an interactive, searchable knowledge graph.
- [codegraph](https://github.com/colbymchenry/codegraph) ![Stars](https://img.shields.io/github/stars/colbymchenry/codegraph?style=social) `Framework` `Infra` - Pre-indexed code knowledge graph for Claude Code, Cursor, Codex.
- [code-review-graph](https://github.com/tirth8205/code-review-graph) ![Stars](https://img.shields.io/github/stars/tirth8205/code-review-graph?style=social) `Framework` `Infra` - Local knowledge graph for Claude Code codebase mapping.
- [QASystemOnMedicalKG](https://github.com/liuhuanyong/QASystemOnMedicalKG) ![Stars](https://img.shields.io/github/stars/liuhuanyong/QASystemOnMedicalKG?style=social) `Framework` `Example` `Infra` - Medical knowledge graph construction and QA system.
- [KnowledgeGraphData](https://github.com/ownthink/KnowledgeGraphData) ![Stars](https://img.shields.io/github/stars/ownthink/KnowledgeGraphData?style=social) `Framework` `Research` `Infra` - 140-million-entity Chinese knowledge graph open dataset.
- [DeepKE](https://github.com/zjunlp/DeepKE) ![Stars](https://img.shields.io/github/stars/zjunlp/DeepKE?style=social) `Framework` `Research` `Infra` - Knowledge graph extraction and construction toolkit (EMNLP 2022).
- [Yuxi](https://github.com/xerrors/Yuxi) ![Stars](https://img.shields.io/github/stars/xerrors/Yuxi?style=social) `Framework` `Infra` - Multi-tenant agent platform integrating LightRAG + knowledge graphs + MCP.

</details>

---

## 02. Agent Brain

### Planning

<details>
<summary><b>Task Decomposition</b> — Breaking goals into subtasks</summary>

- [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) ![Stars](https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=social) `Official` `Framework` `Research` `Infra` - Hierarchical multi-agent system with automated task decomposition.
- [Plan-and-Solve-Prompting](https://github.com/AGI-Edgerunners/Plan-and-Solve-Prompting) ![Stars](https://img.shields.io/github/stars/AGI-Edgerunners/Plan-and-Solve-Prompting?style=social) `Framework` `Research` - Plan-and-Solve prompting (ACL 2023).
- [babyagi](https://github.com/yoheinakajima/babyagi) ![Stars](https://img.shields.io/github/stars/yoheinakajima/babyagi?style=social) `Framework` - Task decomposition and prioritization agent.
- [full-self-coding](https://github.com/NO-CHATBOT-REVOLUTION/full-self-coding) ![Stars](https://img.shields.io/github/stars/NO-CHATBOT-REVOLUTION/full-self-coding?style=social) `Framework` - 100-1000 AI agents coding in parallel with autonomous decomposition.
- [lemon-agent](https://github.com/felixbrock/lemon-agent) ![Stars](https://img.shields.io/github/stars/felixbrock/lemon-agent?style=social) `Framework` - Plan-Validate-Solve agent for workflow automation.
- [ANWS](https://github.com/Haaaiawd/ANWS) ![Stars](https://img.shields.io/github/stars/Haaaiawd/ANWS?style=social) `Framework` - PRD to Architecture to Task decomposition framework.
- [langchain-huggingGPT](https://github.com/camille-vanhoffelen/langchain-huggingGPT) ![Stars](https://img.shields.io/github/stars/camille-vanhoffelen/langchain-huggingGPT?style=social) `Framework` - Langchain HuggingGPT implementation with subtask planning.
- [pi-squad](https://github.com/picassio/pi-squad) ![Stars](https://img.shields.io/github/stars/picassio/pi-squad?style=social) `Framework` - Multi-agent collaboration with task decomposition and parallel execution.
- [SagaLLM](https://github.com/genglongling/SagaLLM) ![Stars](https://img.shields.io/github/stars/genglongling/SagaLLM?style=social) `Framework` - Context management and transaction guarantees for multi-agent planning.
- [HEIM](https://github.com/merocle/HEIM) ![Stars](https://img.shields.io/github/stars/merocle/HEIM?style=social) `Framework` `Infra` - Hybrid Enterprise Inference Mesh with task decomposition and routing.

</details>

<details>
<summary><b>Goal Routing</b> — Semantic routing and intent classification</summary>

- [plano](https://github.com/katanemo/plano) ![Stars](https://img.shields.io/github/stars/katanemo/plano?style=social) `Framework` `Infra` - AI-native proxy with smart LLM routing and orchestration.
- [RouteLLM](https://github.com/lm-sys/RouteLLM) ![Stars](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=social) `Framework` `Research` `Infra` - Framework for serving and evaluating LLM routers.
- [semantic-router](https://github.com/aurelio-labs/semantic-router) ![Stars](https://img.shields.io/github/stars/aurelio-labs/semantic-router?style=social) `Framework` - Superfast AI decision making and semantic routing.
- [semantic-router (vllm)](https://github.com/vllm-project/semantic-router) ![Stars](https://img.shields.io/github/stars/vllm-project/semantic-router?style=social) `Framework` `Infra` - System-level intelligent router for Mixture-of-Models.
- [LLMRouter](https://github.com/ulab-uiuc/LLMRouter) ![Stars](https://img.shields.io/github/stars/ulab-uiuc/LLMRouter?style=social) `Framework` - Open-source library for LLM routing.
- [WilmerAI](https://github.com/SomeOddCodeGuy/WilmerAI) ![Stars](https://img.shields.io/github/stars/SomeOddCodeGuy/WilmerAI?style=social) `Framework` `Infra` - Multi-layer prompt routing for LLM-connected apps.
- [OrcaRouter-Lite](https://github.com/Continuum-AI-Corp/OrcaRouter-Lite) ![Stars](https://img.shields.io/github/stars/Continuum-AI-Corp/OrcaRouter-Lite?style=social) `Framework` - Self-hosted LLM router with managed safety net.
- [UncommonRoute](https://github.com/CommonstackAI/UncommonRoute) ![Stars](https://img.shields.io/github/stars/CommonstackAI/UncommonRoute?style=social) `Framework` `Infra` - Automatic LLM router, 82% cost savings.
- [litellm](https://github.com/BerriAI/litellm) ![Stars](https://img.shields.io/github/stars/BerriAI/litellm?style=social) `Official` `Framework` `Infra` - OpenAI-compatible proxy with provider routing, fallbacks, and spend controls.
- [gateway](https://github.com/Portkey-AI/gateway) ![Stars](https://img.shields.io/github/stars/Portkey-AI/gateway?style=social) `Official` `Framework` `Infra` - AI gateway with routing, guardrails, caching, and observability for LLM apps.

</details>

<details>
<summary><b>Reflection</b> — Self-refinement and verbal reinforcement</summary>

- [reflexion](https://github.com/noahshinn/reflexion) ![Stars](https://img.shields.io/github/stars/noahshinn/reflexion?style=social) `Framework` `Research` - Reflexion: Language Agents with Verbal Reinforcement Learning (NeurIPS 2023).
- [self-rag](https://github.com/AkariAsai/self-rag) ![Stars](https://img.shields.io/github/stars/AkariAsai/self-rag?style=social) `Framework` `Research` - SELF-RAG: Learning to Retrieve, Generate and Critique through self-reflection.
- [self-refine](https://github.com/madaan/self-refine) ![Stars](https://img.shields.io/github/stars/madaan/self-refine?style=social) `Framework` `Research` - LLMs generate feedback and iteratively improve outputs.
- [langgraph-course](https://github.com/emarco177/langgraph-course) ![Stars](https://img.shields.io/github/stars/emarco177/langgraph-course?style=social) `Framework` `Example` `Research` - LangGraph course with reflection workflow patterns.
- [self-correction-llm-papers](https://github.com/teacherpeterpan/self-correction-llm-papers) ![Stars](https://img.shields.io/github/stars/teacherpeterpan/self-correction-llm-papers?style=social) `Framework` `Research` `Infra` - Research papers on self-correcting LLMs.
- [self-reflection](https://github.com/matthewrenze/self-reflection) ![Stars](https://img.shields.io/github/stars/matthewrenze/self-reflection?style=social) `Framework` `Research` - Effects of self-reflection on problem-solving performance.
- [SuperCorrect-llm](https://github.com/YangLing0818/SuperCorrect-llm) ![Stars](https://img.shields.io/github/stars/YangLing0818/SuperCorrect-llm?style=social) `Framework` `Example` `Research` - Thought template distillation and self-correction (ICLR 2025).
- [llm-self-correction-papers](https://github.com/ryokamoi/llm-self-correction-papers) ![Stars](https://img.shields.io/github/stars/ryokamoi/llm-self-correction-papers?style=social) `Framework` `Research` - Curated list of papers on LLM self-correction.
- [langgraph-reflection](https://github.com/langchain-ai/langgraph-reflection) ![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph-reflection?style=social) `Official` `Framework` `Research` `Archived Classic` - LangGraph agent pattern for critique-and-revise reflection loops.
- [socratic-self-refine-reasoning](https://github.com/SalesforceAIResearch/socratic-self-refine-reasoning) ![Stars](https://img.shields.io/github/stars/SalesforceAIResearch/socratic-self-refine-reasoning?style=social) `Official` `Framework` `Research` - Socratic self-refine framework for improving LLM reasoning.

</details>

### Reasoning

<details>
<summary><b>ReAct</b> — Synergizing Reasoning and Acting</summary>

- [ReAct](https://github.com/ysymyth/ReAct) ![Stars](https://img.shields.io/github/stars/ysymyth/ReAct?style=social) `Official` `Research` - Official implementation: ReAct (ICLR 2023).
- [react-agent](https://github.com/eylonmiz/react-agent) ![Stars](https://img.shields.io/github/stars/eylonmiz/react-agent?style=social) `Research` - Open-source autonomous LLM agent implementing ReAct.
- [react-agent (LangGraph)](https://github.com/langchain-ai/react-agent) ![Stars](https://img.shields.io/github/stars/langchain-ai/react-agent?style=social) `Official` `Framework` `Example` `Research` - LangGraph template for a ReAct agent.
- [langgraph-mcp-agents](https://github.com/braincrew-lab/langgraph-mcp-agents) ![Stars](https://img.shields.io/github/stars/braincrew-lab/langgraph-mcp-agents?style=social) `Framework` `Research` `Infra` - ReAct agent with MCP integration and Streamlit UI.
- [CookHero](https://github.com/Decade-qiu/CookHero) ![Stars](https://img.shields.io/github/stars/Decade-qiu/CookHero?style=social) `Framework` `Research` `Infra` - LLM + RAG + ReAct Agent cooking platform.
- [quantalogic](https://github.com/quantalogic/quantalogic) ![Stars](https://img.shields.io/github/stars/quantalogic/quantalogic?style=social) `Framework` `Research` - ReAct-based coding agent framework.
- [LangChain-ReAct-Agent](https://github.com/lhh737/LangChain-ReAct-Agent) ![Stars](https://img.shields.io/github/stars/lhh737/LangChain-ReAct-Agent?style=social) `Framework` `Research` - LangChain/Graph ReAct Agent with RAG and tool calling.
- [llm-ReAct](https://github.com/OceanPresentChao/llm-ReAct) ![Stars](https://img.shields.io/github/stars/OceanPresentChao/llm-ReAct?style=social) `Example` `Research` - Build an LLM ReAct Agent from scratch (tutorial).
- [langgraph](https://github.com/langchain-ai/langgraph) ![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social) `Official` `Framework` `Research` - LangGraph includes prebuilt ReAct-style agent primitives for reasoning and tool use.
- [agent-implementation](https://github.com/mattambrogi/agent-implementation) ![Stars](https://img.shields.io/github/stars/mattambrogi/agent-implementation?style=social) `Research` - Minimal ReAct agent pattern implementation in Python.

</details>

<details>
<summary><b>Tree of Thoughts</b> — Deliberate reasoning via tree search</summary>

- [tree-of-thought-llm](https://github.com/princeton-nlp/tree-of-thought-llm) ![Stars](https://img.shields.io/github/stars/princeton-nlp/tree-of-thought-llm?style=social) `Research` `Infra` - Tree of Thoughts (NeurIPS 2023).
- [tree-of-thoughts](https://github.com/kyegomez/tree-of-thoughts) ![Stars](https://img.shields.io/github/stars/kyegomez/tree-of-thoughts?style=social) `Framework` `Research` `Infra` - Plug-and-play Tree of Thoughts implementation.
- [graph-of-thoughts](https://github.com/spcl/graph-of-thoughts) ![Stars](https://img.shields.io/github/stars/spcl/graph-of-thoughts?style=social) `Official` `Framework` `Research` `Infra` - Graph of Thoughts (ETH Zurich).
- [Neurite](https://github.com/satellitecomponent/Neurite) ![Stars](https://img.shields.io/github/stars/satellitecomponent/Neurite?style=social) `Framework` `Research` `Infra` - Fractal Graph-of-Thought mind-mapping for AI agents.
- [tree-of-thought-prompting](https://github.com/dave1010/tree-of-thought-prompting) ![Stars](https://img.shields.io/github/stars/dave1010/tree-of-thought-prompting?style=social) `Research` `Infra` - Tree-of-Thought prompting to boost reasoning.
- [MindMap](https://github.com/wyl-willing/MindMap) ![Stars](https://img.shields.io/github/stars/wyl-willing/MindMap?style=social) `Framework` `Research` `Infra` - Knowledge Graph Prompting sparks Graph of Thoughts.
- [tree-of-thought-puzzle-solver](https://github.com/jieyilong/tree-of-thought-puzzle-solver) ![Stars](https://img.shields.io/github/stars/jieyilong/tree-of-thought-puzzle-solver?style=social) `Framework` `Research` `Infra` - ToT framework for complex reasoning tasks.
- [knowledge-graph-of-thoughts](https://github.com/spcl/knowledge-graph-of-thoughts) ![Stars](https://img.shields.io/github/stars/spcl/knowledge-graph-of-thoughts?style=social) `Official` `Framework` `Research` `Infra` - Affordable AI Assistants with Knowledge Graph of Thoughts.
- [LanguageAgentTreeSearch](https://github.com/lapisrocks/LanguageAgentTreeSearch) ![Stars](https://img.shields.io/github/stars/lapisrocks/LanguageAgentTreeSearch?style=social) `Official` `Research` `Infra` - ICML 2024 LATS implementation combining tree search, reasoning, acting, and planning.
- [saplings](https://github.com/shobrook/saplings) ![Stars](https://img.shields.io/github/stars/shobrook/saplings?style=social) `Research` `Infra` - Plug-and-play tree search for language agents.

</details>

<details>
<summary><b>Multi-Agent Debate</b> — Collaborative reasoning through debate</summary>

- [Multi-Agents-Debate](https://github.com/Skytliang/Multi-Agents-Debate) ![Stars](https://img.shields.io/github/stars/Skytliang/Multi-Agents-Debate?style=social) `Framework` `Research` - MAD: Multi-Agent Debate with LLMs.
- [ChatEval](https://github.com/thunlp/ChatEval) ![Stars](https://img.shields.io/github/stars/thunlp/ChatEval?style=social) `Framework` `Research` - Better LLM evaluators through multi-agent debate.
- [llm_debate](https://github.com/ucl-dark/llm_debate) ![Stars](https://img.shields.io/github/stars/ucl-dark/llm_debate?style=social) `Framework` `Research` - Debating with More Persuasive LLMs (UCL DARK).
- [magi](https://github.com/fshiori/magi) ![Stars](https://img.shields.io/github/stars/fshiori/magi?style=social) `Framework` `Research` - Three LLMs debate for better decisions.
- [Agent-Debate](https://github.com/starshine-f/Agent-Debate) ![Stars](https://img.shields.io/github/stars/starshine-f/Agent-Debate?style=social) `Framework` `Research` - Multi-agent debate with AI-vs-AI and Human-vs-AI.
- [DebateLLM](https://github.com/instadeepai/DebateLLM) ![Stars](https://img.shields.io/github/stars/instadeepai/DebateLLM?style=social) `Framework` `Research` - Benchmarking multi-agent debate for truthfulness.
- [SWE-Debate](https://github.com/YerbaPage/SWE-Debate) ![Stars](https://img.shields.io/github/stars/YerbaPage/SWE-Debate?style=social) `Framework` `Research` - Competitive debate for software issue resolution (ICSE 2026).
- [M-MAD](https://github.com/SU-JIAYUAN/M-MAD) ![Stars](https://img.shields.io/github/stars/SU-JIAYUAN/M-MAD?style=social) `Framework` `Research` - Multidimensional debate for translation evaluation (ACL 2025).
- [mallm](https://github.com/Multi-Agent-LLMs/mallm) ![Stars](https://img.shields.io/github/stars/Multi-Agent-LLMs/mallm?style=social) `Framework` `Research` - Framework for multi-agent LLM conversational task solving and debate.
- [debate-or-vote](https://github.com/deeplearning-wisc/debate-or-vote) ![Stars](https://img.shields.io/github/stars/deeplearning-wisc/debate-or-vote?style=social) `Official` `Framework` `Research` - NeurIPS 2025 code for comparing debate and voting in multi-agent LLM decisions.

</details>

<details>
<summary><b>Self-Correction</b> — Iterative repair and debugging</summary>

- [SWE-agent](https://github.com/SWE-agent/SWE-agent) ![Stars](https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=social) `Research` - Autonomous agent that fixes GitHub issues (NeurIPS 2024).
- [AlphaCodium](https://github.com/Codium-ai/AlphaCodium) ![Stars](https://img.shields.io/github/stars/Codium-ai/AlphaCodium?style=social) `Official` `Framework` `Research` - Iterative self-correction for code generation.
- [automata](https://github.com/emrgnt-cmplxty/automata) ![Stars](https://img.shields.io/github/stars/emrgnt-cmplxty/automata?style=social) `Framework` `Research` `Archived Classic` - Self-coding agent that writes, executes, and self-corrects.
- [MapCoder](https://github.com/Md-Ashraful-Pramanik/MapCoder) ![Stars](https://img.shields.io/github/stars/Md-Ashraful-Pramanik/MapCoder?style=social) `Framework` `Research` - Multi-agent code generation with self-debugging.
- [STELLA](https://github.com/zaixizhang/STELLA) ![Stars](https://img.shields.io/github/stars/zaixizhang/STELLA?style=social) `Research` `Infra` - Self-evolving LLM agent for biomedical research.
- [DiagGym](https://github.com/MAGIC-AI4Med/DiagGym) ![Stars](https://img.shields.io/github/stars/MAGIC-AI4Med/DiagGym?style=social) `Research` - Virtual clinical environment for self-evolving diagnostic agents.
- [RepairAgent](https://github.com/sola-st/RepairAgent) ![Stars](https://img.shields.io/github/stars/sola-st/RepairAgent?style=social) `Research` - Autonomous LLM-based agent for automated software repair.
- [SE-Agent](https://github.com/JARVIS-Xs/SE-Agent) ![Stars](https://img.shields.io/github/stars/JARVIS-Xs/SE-Agent?style=social) `Framework` `Research` - Self-evolution framework for LLM code agents with revision and refinement.
- [Chronos](https://github.com/Kodezi/Chronos) ![Stars](https://img.shields.io/github/stars/Kodezi/Chronos?style=social) `Framework` `Research` - Debugging-first code model and benchmark report with persistent debug memory.
- [Prometheus](https://github.com/EuniAI/Prometheus) ![Stars](https://img.shields.io/github/stars/EuniAI/Prometheus?style=social) `Framework` `Research` - Knowledge-graph-driven coding agent for reasoning over and repairing complex codebases.

</details>

### Decision Engine

<details>
<summary><b>Tool Selection</b> — Function calling and tool use</summary>

- [gorilla](https://github.com/ShishirPatil/gorilla) ![Stars](https://img.shields.io/github/stars/ShishirPatil/gorilla?style=social) `Framework` `Research` `Infra` - Training and evaluating LLMs for function calls.
- [ToolBench](https://github.com/OpenBMB/ToolBench) ![Stars](https://img.shields.io/github/stars/OpenBMB/ToolBench?style=social) `Framework` `Research` - Open platform for LLM tool learning (ICLR 2024 spotlight).
- [toolformer-pytorch](https://github.com/lucidrains/toolformer-pytorch) ![Stars](https://img.shields.io/github/stars/lucidrains/toolformer-pytorch?style=social) `Framework` `Infra` - Toolformer: Language Models That Can Use Tools.
- [GPTeacher](https://github.com/teknium1/GPTeacher) ![Stars](https://img.shields.io/github/stars/teknium1/GPTeacher?style=social) `Framework` `Research` - Modular datasets including Tool Instruct.
- [lemmy](https://github.com/badlogic/lemmy) ![Stars](https://img.shields.io/github/stars/badlogic/lemmy?style=social) `Framework` - Wrapper for tool-using LLMs in agentic workflows.
- [Hermes-Function-Calling](https://github.com/NousResearch/Hermes-Function-Calling) ![Stars](https://img.shields.io/github/stars/NousResearch/Hermes-Function-Calling?style=social) `Framework` - Tool-use fine-tuning for open-source LLMs.
- [ToolAlpaca](https://github.com/tangqiaoyu/ToolAlpaca) ![Stars](https://img.shields.io/github/stars/tangqiaoyu/ToolAlpaca?style=social) `Official` `Framework` - Generalized tool learning with 3000 simulated cases.
- [mcp-bench](https://github.com/Accenture/mcp-bench) ![Stars](https://img.shields.io/github/stars/Accenture/mcp-bench?style=social) `Framework` `Research` `Infra` - Benchmarking tool-using agents via MCP servers.
- [Graph_Toolformer](https://github.com/jwzhanggy/Graph_Toolformer) ![Stars](https://img.shields.io/github/stars/jwzhanggy/Graph_Toolformer?style=social) `Framework` `Research` - Tool-augmented LLM for graph reasoning.
- [ai](https://github.com/vercel/ai) ![Stars](https://img.shields.io/github/stars/vercel/ai?style=social) `Framework` - TypeScript AI SDK with first-class tool calling for agentic applications.

</details>

<details>
<summary><b>Memory Retrieval</b> — Context and memory management for agents</summary>

- [mem0](https://github.com/mem0ai/mem0) ![Stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social) `Official` `Framework` `Research` - Universal memory layer for AI agents.
- [llama_index](https://github.com/run-llama/llama_index) ![Stars](https://img.shields.io/github/stars/run-llama/llama_index?style=social) `Official` `Framework` `Research` `Infra` - Leading document agent and retrieval platform.
- [letta](https://github.com/letta-ai/letta) ![Stars](https://img.shields.io/github/stars/letta-ai/letta?style=social) `Official` `Framework` `Research` - Stateful agents with advanced memory (formerly MemGPT).
- [haystack](https://github.com/deepset-ai/haystack) ![Stars](https://img.shields.io/github/stars/deepset-ai/haystack?style=social) `Official` `Framework` `Research` `Infra` - AI orchestration with retrieval, routing, and memory.
- [txtai](https://github.com/neuml/txtai) ![Stars](https://img.shields.io/github/stars/neuml/txtai?style=social) `Framework` `Research` `Infra` - All-in-one framework for semantic search and LLM workflows.
- [zep](https://github.com/getzep/zep) ![Stars](https://img.shields.io/github/stars/getzep/zep?style=social) `Official` `Framework` `Example` `Research` `Infra` - Long-term memory and context management for AI assistants.
- [langmem](https://github.com/langchain-ai/langmem) ![Stars](https://img.shields.io/github/stars/langchain-ai/langmem?style=social) `Official` `Framework` `Research` - LangChain memory primitives for LLM agents.
- [memvid](https://github.com/memvid/memvid) ![Stars](https://img.shields.io/github/stars/memvid/memvid?style=social) `Framework` `Research` `Infra` - Single-file video-backed memory and retrieval for RAG-style agents.
- [ragflow](https://github.com/infiniflow/ragflow) ![Stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social) `Official` `Framework` `Research` `Infra` - Open-source RAG engine with document understanding and agent retrieval.
- [graphiti](https://github.com/getzep/graphiti) ![Stars](https://img.shields.io/github/stars/getzep/graphiti?style=social) `Official` `Framework` `Research` - Temporal knowledge graph memory for AI agents.

</details>

<details>
<summary><b>Action Prioritization</b> — Orchestration and workflow engines</summary>

- [conductor](https://github.com/conductor-oss/conductor) ![Stars](https://img.shields.io/github/stars/conductor-oss/conductor?style=social) `Framework` `Research` - Event-driven agentic workflow engine with durable execution.
- [swarm](https://github.com/openai/swarm) ![Stars](https://img.shields.io/github/stars/openai/swarm?style=social) `Official` `Framework` - Lightweight multi-agent orchestration (OpenAI).
- [agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) ![Stars](https://img.shields.io/github/stars/ComposioHQ/agent-orchestrator?style=social) `Official` `Framework` - Parallel coding agents with autonomous orchestration.
- [swarms](https://github.com/kyegomez/swarms) ![Stars](https://img.shields.io/github/stars/kyegomez/swarms?style=social) `Framework` - Enterprise-grade multi-agent orchestration framework.
- [open-multi-agent](https://github.com/open-multi-agent/open-multi-agent) ![Stars](https://img.shields.io/github/stars/open-multi-agent/open-multi-agent?style=social) `Framework` - Goal to task DAG, TypeScript-native multi-agent orchestration.
- [mission-control](https://github.com/builderz-labs/mission-control) ![Stars](https://img.shields.io/github/stars/builderz-labs/mission-control?style=social) `Framework` `Infra` - Self-hosted AI agent orchestration platform.
- [agency-swarm](https://github.com/VRSEN/agency-swarm) ![Stars](https://img.shields.io/github/stars/VRSEN/agency-swarm?style=social) `Framework` - Reliable multi-agent orchestration framework.
- [langgraph](https://github.com/langchain-ai/langgraph) ![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social) `Official` `Framework` - Graph-based state machine for prioritizing and controlling agent actions.
- [temporal](https://github.com/temporalio/temporal) ![Stars](https://img.shields.io/github/stars/temporalio/temporal?style=social) `Framework` `Infra` - Durable workflow engine for reliable long-running agent action queues.
- [prefect](https://github.com/PrefectHQ/prefect) ![Stars](https://img.shields.io/github/stars/PrefectHQ/prefect?style=social) `Framework` - Workflow orchestration engine for scheduling, retries, and prioritizing agent tasks.

</details>

---

## 03. Tool Layer

### Web Search

<details>
<summary><b>Web Search</b> — Search APIs and web scraping tools for AI agents</summary>

- [firecrawl](https://github.com/firecrawl/firecrawl) ![Stars](https://img.shields.io/github/stars/firecrawl/firecrawl?style=social) `Official` `Infra` - Search, scrape, and clean the web for AI agents. Turn any website into clean Markdown for LLMs.
- [deep-research](https://github.com/dzhng/deep-research) ![Stars](https://img.shields.io/github/stars/dzhng/deep-research?style=social) `Framework` `Research` `Infra` - AI-powered research assistant combining search engines, web scraping, and LLMs.
- [DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) ![Stars](https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=social) `Official` `Research` `Infra` - Tongyi Deep Research — leading open-source Deep Research Agent from Alibaba.
- [morphic](https://github.com/miurla/morphic) ![Stars](https://img.shields.io/github/stars/miurla/morphic?style=social) `Framework` `Research` `Infra` - AI-powered search engine with generative UI (Perplexity-style open-source alternative).
- [MiroThinker](https://github.com/MiroMindAI/MiroThinker) ![Stars](https://img.shields.io/github/stars/MiroMindAI/MiroThinker?style=social) `Official` `Framework` `Research` `Infra` - Deep research agent optimized for complex research and prediction tasks.
- [firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) ![Stars](https://img.shields.io/github/stars/firecrawl/firecrawl-mcp-server?style=social) `Official` `Framework` `Infra` - Official Firecrawl MCP Server for Cursor, Claude, and any LLM client.
- [open-deep-research](https://github.com/nickscamara/open-deep-research) ![Stars](https://img.shields.io/github/stars/nickscamara/open-deep-research?style=social) `Example` `Research` `Infra` - Open-source deep research clone with Firecrawl integration.
- [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) ![Stars](https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=social) `Official` `Framework` `Research` `Infra` - Hierarchical multi-agent system for deep research with automated task decomposition.
- [tavily-mcp](https://github.com/tavily-ai/tavily-mcp) ![Stars](https://img.shields.io/github/stars/tavily-ai/tavily-mcp?style=social) `Official` `Infra` - Production-ready MCP server with real-time search, extract, map and crawl.
- [fireplexity](https://github.com/firecrawl/fireplexity) ![Stars](https://img.shields.io/github/stars/firecrawl/fireplexity?style=social) `Official` `Framework` `Infra` - Open-source Perplexity-like AI search engine with real-time citations.

</details>

### Browser Automation

<details>
<summary><b>Browser Automation</b> — Web browsing and browser control for AI agents</summary>

- [browser-use](https://github.com/browser-use/browser-use) ![Stars](https://img.shields.io/github/stars/browser-use/browser-use?style=social) `Official` `Infra` - Make websites accessible for AI agents. Automate tasks online with ease.
- [agent-browser](https://github.com/vercel-labs/agent-browser) ![Stars](https://img.shields.io/github/stars/vercel-labs/agent-browser?style=social) `Infra` - Browser automation CLI for AI agents.
- [agenticSeek](https://github.com/Fosowl/agenticSeek) ![Stars](https://img.shields.io/github/stars/Fosowl/agenticSeek?style=social) `Official` `Infra` - Fully Local Manus AI. Autonomous agent that thinks, browses the web, and codes.
- [nanobrowser](https://github.com/nanobrowser/nanobrowser) ![Stars](https://img.shields.io/github/stars/nanobrowser/nanobrowser?style=social) `Framework` `Infra` - Open-source Chrome extension for AI-powered web automation with multi-agent workflows.
- [openbrowser](https://github.com/ntegrals/openbrowser) ![Stars](https://img.shields.io/github/stars/ntegrals/openbrowser?style=social) `Framework` `Infra` - Autonomous toolkit for browser-based AI agents.
- [steel-browser](https://github.com/steel-dev/steel-browser) ![Stars](https://img.shields.io/github/stars/steel-dev/steel-browser?style=social) `Infra` - Open Source Browser API for AI Agents & Apps. Batteries-included browser sandbox.
- [LaVague](https://github.com/lavague-ai/LaVague) ![Stars](https://img.shields.io/github/stars/lavague-ai/LaVague?style=social) `Framework` `Infra` - Large Action Model framework to develop AI Web Agents.
- [camofox-browser](https://github.com/jo-inc/camofox-browser) ![Stars](https://img.shields.io/github/stars/jo-inc/camofox-browser?style=social) `Infra` - Stealth headless browser for AI agents — bypass Cloudflare bot detection.
- [openagent](https://github.com/the-open-agent/openagent) ![Stars](https://img.shields.io/github/stars/the-open-agent/openagent?style=social) `Infra` - Personal AI assistant with computer-use, browser-use, and coding agent support.
- [browser-agent](https://github.com/magnitudedev/browser-agent) ![Stars](https://img.shields.io/github/stars/magnitudedev/browser-agent?style=social) `Infra` - Open-source vision-first browser agent.

</details>

### Code Execution

<details>
<summary><b>Code Execution</b> — Sandboxes and code interpreters for AI agents</summary>

- [daytona](https://github.com/daytonaio/daytona) ![Stars](https://img.shields.io/github/stars/daytonaio/daytona?style=social) `Framework` `Infra` - Secure and elastic infrastructure for running AI-generated code.
- [open-interpreter](https://github.com/openinterpreter/open-interpreter) ![Stars](https://img.shields.io/github/stars/openinterpreter/open-interpreter?style=social) `Infra` - Natural language interface for computers — lets LLMs run code locally.
- [E2B](https://github.com/e2b-dev/E2B) ![Stars](https://img.shields.io/github/stars/e2b-dev/E2B?style=social) `Official` `Research` `Infra` - Open-source secure sandboxed cloud environment for enterprise-grade AI agents.
- [jupyter-ai](https://github.com/jupyterlab/jupyter-ai) ![Stars](https://img.shields.io/github/stars/jupyterlab/jupyter-ai?style=social) `Example` `Infra` - AI agents connected to computational notebooks in JupyterLab.
- [judge0](https://github.com/judge0/judge0) ![Stars](https://img.shields.io/github/stars/judge0/judge0?style=social) `Framework` `Infra` - Robust, fast, scalable, and sandboxed online code execution system.
- [arrow-js](https://github.com/standardagents/arrow-js) ![Stars](https://img.shields.io/github/stars/standardagents/arrow-js?style=social) `Framework` `Research` `Infra` - UI framework for the agentic era with WASM sandboxes for safe code execution.
- [code-interpreter](https://github.com/e2b-dev/code-interpreter) ![Stars](https://img.shields.io/github/stars/e2b-dev/code-interpreter?style=social) `Official` `Framework` `Example` `Infra` - Python & JS/TS SDK for running AI-generated code in your AI app.
- [dify-sandbox](https://github.com/langgenius/dify-sandbox) ![Stars](https://img.shields.io/github/stars/langgenius/dify-sandbox?style=social) `Infra` - Lightweight, fast, and secure code execution environment (from the Dify team).
- [arrakis](https://github.com/abshkbh/arrakis) ![Stars](https://img.shields.io/github/stars/abshkbh/arrakis?style=social) `Framework` `Infra` - Self-hosted sandboxing for AI agent code execution with MicroVM isolation.
- [SmolVM](https://github.com/CelestoAI/SmolVM) ![Stars](https://img.shields.io/github/stars/CelestoAI/SmolVM?style=social) `Framework` `Infra` - Open-source AI sandbox infrastructure for code execution, browser use, and AI agents.

</details>

### API Integration

<details>
<summary><b>API Integration</b> — MCP servers, tool connectors, and API frameworks for agents</summary>

- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) ![Stars](https://img.shields.io/github/stars/punkpeye/awesome-mcp-servers?style=social) `Framework` `Research` `Infra` - Curated collection of MCP servers.
- [servers](https://github.com/modelcontextprotocol/servers) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=social) `Official` `Framework` `Infra` - Official Model Context Protocol reference servers.
- [playwright-mcp](https://github.com/microsoft/playwright-mcp) ![Stars](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=social) `Official` `Framework` `Infra` - Playwright MCP server — browser automation for AI agents.
- [github-mcp-server](https://github.com/github/github-mcp-server) ![Stars](https://img.shields.io/github/stars/github/github-mcp-server?style=social) `Official` `Framework` `Infra` - GitHub's official MCP Server for AI agent integration.
- [fastmcp](https://github.com/PrefectHQ/fastmcp) ![Stars](https://img.shields.io/github/stars/PrefectHQ/fastmcp?style=social) `Framework` `Infra` - The fast, Pythonic way to build MCP servers and clients.
- [python-sdk](https://github.com/modelcontextprotocol/python-sdk) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/python-sdk?style=social) `Official` `Framework` `Infra` - Official Python SDK for MCP servers and clients.
- [activepieces](https://github.com/activepieces/activepieces) ![Stars](https://img.shields.io/github/stars/activepieces/activepieces?style=social) `Framework` `Infra` - AI Agents, MCPs, and AI Workflow Automation (~400 MCP servers).
- [mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) ![Stars](https://img.shields.io/github/stars/microsoft/mcp-for-beginners?style=social) `Official` `Framework` `Example` `Infra` - Open-source MCP curriculum with cross-language examples.
- [mcp-toolbox](https://github.com/googleapis/mcp-toolbox) ![Stars](https://img.shields.io/github/stars/googleapis/mcp-toolbox?style=social) `Official` `Framework` `Research` `Infra` - Google's open-source MCP server for databases.
- [Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) ![Stars](https://img.shields.io/github/stars/GLips/Figma-Context-MCP?style=social) `Framework` `Infra` - MCP server providing Figma layout info to AI coding agents.

</details>

### Database Access

<details>
<summary><b>Database Access</b> — Text-to-SQL, database agents, and NL2SQL tools</summary>

- [vanna](https://github.com/vanna-ai/vanna) ![Stars](https://img.shields.io/github/stars/vanna-ai/vanna?style=social) `Official` `Framework` `Research` `Infra` `Archived Classic` - Chat with your SQL database. Accurate Text-to-SQL via LLMs using Agentic RAG.
- [WrenAI](https://github.com/Canner/WrenAI) ![Stars](https://img.shields.io/github/stars/Canner/WrenAI?style=social) `Framework` `Infra` - Turn AI Agents into data analysts. Text-to-SQL, dashboards, agentic analytics across 20+ data sources.
- [SQLBot](https://github.com/dataease/SQLBot) ![Stars](https://img.shields.io/github/stars/dataease/SQLBot?style=social) `Framework` `Infra` - Intelligent data querying based on LLMs and RAG. Conversational data analysis.
- [Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL) ![Stars](https://img.shields.io/github/stars/eosphoros-ai/Awesome-Text2SQL?style=social) `Framework` `Example` `Research` `Infra` - Curated tutorials and resources for Text2SQL, Text2DSL, Text2API, Text2Vis.
- [DB-GPT-Hub](https://github.com/eosphoros-ai/DB-GPT-Hub) ![Stars](https://img.shields.io/github/stars/eosphoros-ai/DB-GPT-Hub?style=social) `Framework` `Research` `Infra` - Models, datasets, and fine-tuning techniques for Text-to-SQL.
- [NL2SQL](https://github.com/yechens/NL2SQL) ![Stars](https://img.shields.io/github/stars/yechens/NL2SQL?style=social) `Framework` `Research` `Infra` - Text2SQL semantic parsing datasets, solutions, and paper resources.
- [NL2SQL_Handbook](https://github.com/HKUSTDial/NL2SQL_Handbook) ![Stars](https://img.shields.io/github/stars/HKUSTDial/NL2SQL_Handbook?style=social) `Framework` `Research` `Infra` - Continuously updated handbook for latest Text-to-SQL techniques.
- [Awesome-LLM-based-Text2SQL](https://github.com/DEEP-PolyU/Awesome-LLM-based-Text2SQL) ![Stars](https://img.shields.io/github/stars/DEEP-PolyU/Awesome-LLM-based-Text2SQL?style=social) `Framework` `Research` `Infra` - TKDE 2025 survey: Next-Generation Database Interfaces.
- [spider](https://github.com/taoyds/spider) ![Stars](https://img.shields.io/github/stars/taoyds/spider?style=social) `Framework` `Research` `Infra` - Yale complex and cross-domain semantic parsing and text-to-SQL benchmark.
- [BIRD-Interact](https://github.com/bird-bench/BIRD-Interact) ![Stars](https://img.shields.io/github/stars/bird-bench/BIRD-Interact?style=social) `Framework` `Research` `Infra` - ICLR 2026 Oral. Re-imagines Text-to-SQL evaluation via dynamic interactions.

</details>

### File System

<details>
<summary><b>File System</b> — Document processing, parsing, and unstructured data tools</summary>

- [marker](https://github.com/datalab-to/marker) ![Stars](https://img.shields.io/github/stars/datalab-to/marker?style=social) `Framework` `Infra` - Convert PDF to markdown + JSON quickly with high accuracy.
- [MonkeyOCR](https://github.com/Yuliang-Liu/MonkeyOCR) ![Stars](https://img.shields.io/github/stars/Yuliang-Liu/MonkeyOCR?style=social) `Framework` `Infra` - Lightweight LMM-based document parsing model.
- [unstract](https://github.com/Zipstack/unstract) ![Stars](https://img.shields.io/github/stars/Zipstack/unstract?style=social) `Framework` `Infra` - LLM-Driven extraction of unstructured data with API deployments & ETL pipelines.
- [liteparse](https://github.com/run-llama/liteparse) ![Stars](https://img.shields.io/github/stars/run-llama/liteparse?style=social) `Official` `Framework` `Infra` - Fast, helpful, and open-source document parser by LlamaIndex.
- [llm-graph-builder](https://github.com/neo4j-labs/llm-graph-builder) ![Stars](https://img.shields.io/github/stars/neo4j-labs/llm-graph-builder?style=social) `Framework` `Infra` - Neo4j graph construction from unstructured data using LLMs.
- [datachain](https://github.com/datachain-ai/datachain) ![Stars](https://img.shields.io/github/stars/datachain-ai/datachain?style=social) `Framework` `Research` `Infra` - Context layer for unstructured data: typed, versioned datasets over S3, GCS, Azure.
- [OCRFlux](https://github.com/chatdoc-com/OCRFlux) ![Stars](https://img.shields.io/github/stars/chatdoc-com/OCRFlux?style=social) `Framework` `Infra` - Multimodal toolkit for PDF-to-Markdown with complex layout and table parsing.
- [docext](https://github.com/NanoNets/docext) ![Stars](https://img.shields.io/github/stars/NanoNets/docext?style=social) `Framework` `Infra` - On-premises, OCR-free unstructured data extraction and markdown conversion.
- [semtools](https://github.com/run-llama/semtools) ![Stars](https://img.shields.io/github/stars/run-llama/semtools?style=social) `Official` `Framework` `Infra` - Semantic search and document parsing tools for the command line.
- [OmniDocBench](https://github.com/opendatalab/OmniDocBench) ![Stars](https://img.shields.io/github/stars/opendatalab/OmniDocBench?style=social) `Framework` `Research` `Infra` - CVPR 2025 — Comprehensive benchmark for document parsing and evaluation.

</details>

---

## 04. Agent Workflows

### Research Agent

<details>
<summary><b>Research Agent</b> — Automated research, deep research, and paper discovery agents</summary>

- [storm](https://github.com/stanford-oval/storm) ![Stars](https://img.shields.io/github/stars/stanford-oval/storm?style=social) `Official` `Framework` `Research` `Infra` - LLM-powered knowledge curation system that researches a topic and generates full-length reports with citations.
- [gpt-researcher](https://github.com/assafelovic/gpt-researcher) ![Stars](https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=social) `Framework` `Research` `Infra` - Autonomous agent that conducts deep research on any topic using any LLM provider.
- [deep-research](https://github.com/dzhng/deep-research) ![Stars](https://img.shields.io/github/stars/dzhng/deep-research?style=social) `Framework` `Research` `Infra` - AI-powered research assistant combining search engines, web scraping, and LLMs.
- [DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) ![Stars](https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=social) `Official` `Framework` `Research` `Infra` - Tongyi Deep Research — leading open-source Deep Research Agent from Alibaba.
- [MiroThinker](https://github.com/MiroMindAI/MiroThinker) ![Stars](https://img.shields.io/github/stars/MiroMindAI/MiroThinker?style=social) `Official` `Framework` `Research` `Infra` - Deep research agent optimized for complex research and prediction tasks.
- [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) ![Stars](https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=social) `Official` `Framework` `Research` `Infra` - Hierarchical multi-agent system for deep research with automated task decomposition.
- [ai-research-assistant](https://github.com/lifan0127/ai-research-assistant) ![Stars](https://img.shields.io/github/stars/lifan0127/ai-research-assistant?style=social) `Framework` `Research` `Infra` - Aria: AI Research Assistant powered by GPT Large Language Models.
- [NanoResearch](https://github.com/OpenRaiser/NanoResearch) ![Stars](https://img.shields.io/github/stars/OpenRaiser/NanoResearch?style=social) `Official` `Framework` `Research` `Infra` - The Autonomous AI Research Assistant.
- [DeepGit](https://github.com/zamalali/DeepGit) ![Stars](https://img.shields.io/github/stars/zamalali/DeepGit?style=social) `Framework` `Research` `Infra` - Deep research agent to find the best GitHub repositories.
- [deep_research_bench](https://github.com/Ayanami0730/deep_research_bench) ![Stars](https://img.shields.io/github/stars/Ayanami0730/deep_research_bench?style=social) `Framework` `Research` `Infra` - Comprehensive Benchmark for Deep Research Agents.

</details>

### Coding Agent

<details>
<summary><b>Coding Agent</b> — Autonomous coding and software engineering agents</summary>

- [opencode](https://github.com/anomalyco/opencode) ![Stars](https://img.shields.io/github/stars/anomalyco/opencode?style=social) `Framework` - The open source coding agent.
- [claude-code](https://github.com/anthropics/claude-code) ![Stars](https://img.shields.io/github/stars/anthropics/claude-code?style=social) `Official` `Framework` - Agentic coding tool that lives in your terminal, understands your codebase.
- [codex](https://github.com/openai/codex) ![Stars](https://img.shields.io/github/stars/openai/codex?style=social) `Official` `Framework` - Lightweight coding agent that runs in your terminal.
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) ![Stars](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=social) `Framework` - AI-Driven Development platform.
- [cline](https://github.com/cline/cline) ![Stars](https://img.shields.io/github/stars/cline/cline?style=social) `Framework` - Autonomous coding agent as SDK, IDE extension, or CLI assistant.
- [aider](https://github.com/Aider-AI/aider) ![Stars](https://img.shields.io/github/stars/Aider-AI/aider?style=social) `Framework` - AI pair programming in your terminal.
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) ![Stars](https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=social) `Framework` `Research` - Takes a GitHub issue and tries to automatically fix it (NeurIPS 2024).
- [DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) ![Stars](https://img.shields.io/github/stars/Hmbown/DeepSeek-TUI?style=social) `Framework` - Coding agent for DeepSeek models that runs in your terminal.
- [claude-coder](https://github.com/kodu-ai/claude-coder) ![Stars](https://img.shields.io/github/stars/kodu-ai/claude-coder?style=social) `Framework` - Autonomous coding agent that lives in your IDE (VSCode extension).
- [OpenAlpha_Evolve](https://github.com/shyamsaktawat/OpenAlpha_Evolve) ![Stars](https://img.shields.io/github/stars/shyamsaktawat/OpenAlpha_Evolve?style=social) `Framework` `Research` `Infra` - Open-source framework inspired by DeepMind's AlphaEvolve for autonomous coding.

</details>

### Sales Agent

<details>
<summary><b>Sales Agent</b> — Sales automation, outreach, and lead generation agents</summary>

- [SalesGPT](https://github.com/filip-michalsky/SalesGPT) ![Stars](https://img.shields.io/github/stars/filip-michalsky/SalesGPT?style=social) `Framework` - Context-aware AI Sales Agent to automate sales outreach.
- [Knotie-AI](https://github.com/avijeett007/Knotie-AI) ![Stars](https://img.shields.io/github/stars/avijeett007/Knotie-AI?style=social) `Framework` - Open-source inbound/outbound AI Sales Agent for lead/customer communication.
- [b2b-sdr-agent-template](https://github.com/iPythoning/b2b-sdr-agent-template) ![Stars](https://img.shields.io/github/stars/iPythoning/b2b-sdr-agent-template?style=social) `Framework` `Example` `Infra` - Open-source AI SDR template for B2B: 10-stage pipeline, multi-channel outreach.
- [sales-ai-agent-langgraph](https://github.com/lucasboscatti/sales-ai-agent-langgraph) ![Stars](https://img.shields.io/github/stars/lucasboscatti/sales-ai-agent-langgraph?style=social) `Framework` - Virtual Sales Agent using LangChain, LangGraph, and Gemini Flash.
- [AI-Sales-agent](https://github.com/kaymen99/AI-Sales-agent) ![Stars](https://img.shields.io/github/stars/kaymen99/AI-Sales-agent?style=social) `Framework` - Sales AI agent with product recommendations, consultations, and Stripe payments.
- [cold-email-ai](https://github.com/bdcorps/cold-email-ai) ![Stars](https://img.shields.io/github/stars/bdcorps/cold-email-ai?style=social) `Framework` - AI-powered cold email generation and outreach system.
- [SalesAgent](https://github.com/MiuLab/SalesAgent) ![Stars](https://img.shields.io/github/stars/MiuLab/SalesAgent?style=social) `Framework` `Research` `Infra` - SalesBot 2.0 — research-oriented AI sales dialogue agent.
- [sales-outreach-automation-langgraph](https://github.com/kaymen99/sales-outreach-automation-langgraph) ![Stars](https://img.shields.io/github/stars/kaymen99/sales-outreach-automation-langgraph?style=social) `Framework` `Research` `Infra` - LangGraph agents for lead research, qualification, personalized outreach, and CRM updates.
- [ai-sdr-bdr-agent](https://github.com/brightdata/ai-sdr-bdr-agent) ![Stars](https://img.shields.io/github/stars/brightdata/ai-sdr-bdr-agent?style=social) `Framework` `Infra` - AI BDR/SDR system for lead discovery, trigger detection, outreach, and CRM integration.
- [SDR-Agent](https://github.com/Deepan-mn/SDR-Agent) ![Stars](https://img.shields.io/github/stars/Deepan-mn/SDR-Agent?style=social) `Framework` - Sales development representative agent for identifying and qualifying leads.

</details>

### Customer Support Agent

<details>
<summary><b>Customer Support Agent</b> — Helpdesk, chatbot, and service agents</summary>

- [Flowise](https://github.com/FlowiseAI/Flowise) ![Stars](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=social) `Framework` `Research` - Build AI Agents visually. Drag-and-drop platform for LLM-powered chatbots and agents.
- [chatwoot](https://github.com/chatwoot/chatwoot) ![Stars](https://img.shields.io/github/stars/chatwoot/chatwoot?style=social) `Framework` - Open-source omni-channel customer support desk. Alternative to Intercom, Zendesk.
- [rasa](https://github.com/RasaHQ/rasa) ![Stars](https://img.shields.io/github/stars/RasaHQ/rasa?style=social) `Framework` - Open source ML framework for text- and voice-based conversational AI.
- [botpress](https://github.com/botpress/botpress) ![Stars](https://img.shields.io/github/stars/botpress/botpress?style=social) `Framework` `Infra` - Open-source hub to build and deploy GPT/LLM conversational agents.
- [cossistant](https://github.com/cossistantcom/cossistant) ![Stars](https://img.shields.io/github/stars/cossistantcom/cossistant?style=social) `Framework` - Open-source customer support platform with customizable AI support agents.
- [tiledesk-server](https://github.com/Tiledesk/tiledesk-server) ![Stars](https://img.shields.io/github/stars/Tiledesk/tiledesk-server?style=social) `Framework` `Infra` - Open-source alternative to Voiceflow with LLM-powered agents and human-in-the-loop.
- [openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) ![Stars](https://img.shields.io/github/stars/openai/openai-cs-agents-demo?style=social) `Official` `Framework` `Example` - Customer service specialist-agent demo built with the OpenAI Agents SDK.
- [openai-realtime-agents](https://github.com/openai/openai-realtime-agents) ![Stars](https://img.shields.io/github/stars/openai/openai-realtime-agents?style=social) `Official` `Framework` `Example` `Infra` - Realtime voice-agent patterns for customer service handoffs and support flows.
- [ai-agents](https://github.com/chatwoot/ai-agents) ![Stars](https://img.shields.io/github/stars/chatwoot/ai-agents?style=social) `Framework` `Example` - Ruby multi-agent SDK with ISP support and customer service examples.
- [ai-customer-support](https://github.com/tushcmd/ai-customer-support) ![Stars](https://img.shields.io/github/stars/tushcmd/ai-customer-support?style=social) `Framework` `Infra` - Next.js AI customer support chatbot with auth, database, and feedback.

</details>

### Content Agent

<details>
<summary><b>Content Agent</b> — Content generation, writing, and creative agents</summary>

- [xhs_content_agent](https://github.com/hl897tech/xhs_content_agent) ![Stars](https://img.shields.io/github/stars/hl897tech/xhs_content_agent?style=social) `Framework` - LLM-based Xiaohongshu (RED) content operation Agent: trend analysis, copywriting, image generation, and publishing.
- [ai-creator](https://github.com/gongxings/ai-creator) ![Stars](https://img.shields.io/github/stars/gongxings/ai-creator?style=social) `Framework` - AI content creation platform with writing, image, video, PPT generation and multi-platform publishing.
- [sage-x-agent](https://github.com/sharbelxyz/sage-x-agent) ![Stars](https://img.shields.io/github/stars/sharbelxyz/sage-x-agent?style=social) `Framework` - X (Twitter) content agent: voice calibration, tweet drafting, thread writing, trend scouting.
- [blog-writing-agent](https://github.com/campusx-official/blog-writing-agent) ![Stars](https://img.shields.io/github/stars/campusx-official/blog-writing-agent?style=social) `Framework` - LangGraph-based blog writing agent.
- [video-content-agent](https://github.com/sailorworks/video-content-agent) ![Stars](https://img.shields.io/github/stars/sailorworks/video-content-agent?style=social) `Framework` - End-to-end AI agent turning topics into viral short videos.
- [content-agent](https://github.com/qiuxchao/content-agent) ![Stars](https://img.shields.io/github/stars/qiuxchao/content-agent?style=social) `Framework` `Infra` - Auto-search materials, generate articles for WeChat/Xiaohongshu/Zhihu. Based on LangGraph.
- [citedy-seo-agent](https://github.com/citedy/citedy-seo-agent) ![Stars](https://img.shields.io/github/stars/citedy/citedy-seo-agent?style=social) `Framework` - AI-powered SEO content automation: trend scouting, article generation in 55 languages.
- [social-media-agent](https://github.com/langchain-ai/social-media-agent) ![Stars](https://img.shields.io/github/stars/langchain-ai/social-media-agent?style=social) `Official` `Framework` - LangGraph agent for sourcing, curating, and scheduling social posts with HITL.
- [10x-Content-Expert](https://github.com/OpenAnalystInc/10x-Content-Expert) ![Stars](https://img.shields.io/github/stars/OpenAnalystInc/10x-Content-Expert?style=social) `Framework` - Claude Code skills plugin for brand-aligned emails, posts, decks, and blogs.
- [social-agents](https://github.com/zxkane/social-agents) ![Stars](https://img.shields.io/github/stars/zxkane/social-agents?style=social) `Framework` - Multi-platform social media automation agents powered by Claude Agent SDK.

</details>

### Autonomous Workflows

<details>
<summary><b>Autonomous Workflows</b> — General-purpose autonomous agent platforms and workflow engines</summary>

- [dify](https://github.com/langgenius/dify) ![Stars](https://img.shields.io/github/stars/langgenius/dify?style=social) `Framework` - Production-ready platform for agentic workflow development with orchestration, RAG, and agents.
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) ![Stars](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT?style=social) `Framework` `Infra` - Experimental open-source autonomous AI agent — the original AutoGPT.
- [conductor](https://github.com/conductor-oss/conductor) ![Stars](https://img.shields.io/github/stars/conductor-oss/conductor?style=social) `Framework` `Research` - Event-driven agentic workflow engine with durable, resilient execution.
- [openai-agents-python](https://github.com/openai/openai-agents-python) ![Stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=social) `Official` `Framework` - Lightweight, powerful framework for multi-agent workflows (OpenAI Agents SDK).
- [haystack](https://github.com/deepset-ai/haystack) ![Stars](https://img.shields.io/github/stars/deepset-ai/haystack?style=social) `Official` `Framework` `Research` `Infra` - Open-source AI orchestration for context-engineered LLM applications.
- [opik](https://github.com/comet-ml/opik) ![Stars](https://img.shields.io/github/stars/comet-ml/opik?style=social) `Framework` `Example` `Research` `Infra` - Debug, evaluate, and monitor LLM applications and agentic workflows.
- [agent-framework](https://github.com/microsoft/agent-framework) ![Stars](https://img.shields.io/github/stars/microsoft/agent-framework?style=social) `Official` `Framework` `Infra` - Framework for building, orchestrating and deploying AI agents (Python and .NET).
- [open-agent-builder](https://github.com/firecrawl/open-agent-builder) ![Stars](https://img.shields.io/github/stars/firecrawl/open-agent-builder?style=social) `Official` `Framework` `Infra` - Visual workflow builder for AI agent pipelines and web data workflows.
- [agent-fleet-o](https://github.com/escapeboy/agent-fleet-o) ![Stars](https://img.shields.io/github/stars/escapeboy/agent-fleet-o?style=social) `Framework` `Infra` - Self-hosted mission control for visual DAG agent workflows and MCP tools.
- [llama-agents](https://github.com/run-llama/llama-agents) ![Stars](https://img.shields.io/github/stars/run-llama/llama-agents?style=social) `Official` `Framework` - Event-driven async workflow framework for LlamaIndex agents.

</details>

---

## 05. Multi-Agent Systems

### Manager Agents

<details>
<summary><b>Manager Agents</b> — Orchestration, supervisor, and routing patterns for multi-agent systems</summary>

- [autogen](https://github.com/microsoft/autogen) ![Stars](https://img.shields.io/github/stars/microsoft/autogen?style=social) `Official` `Framework` - Programming framework for agentic AI with multi-agent conversation and orchestration.
- [crewAI](https://github.com/crewAIInc/crewAI) ![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=social) `Official` `Framework` - Framework for orchestrating role-playing, autonomous AI agents.
- [agno](https://github.com/agno-agi/agno) ![Stars](https://img.shields.io/github/stars/agno-agi/agno?style=social) `Framework` - Build, run, and manage agent platforms with multi-agent orchestration (formerly Phidata).
- [langgraph](https://github.com/langchain-ai/langgraph) ![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social) `Official` `Framework` - Graph-based agent orchestration with supervisor/swarm patterns.
- [semantic-kernel](https://github.com/microsoft/semantic-kernel) ![Stars](https://img.shields.io/github/stars/microsoft/semantic-kernel?style=social) `Official` `Framework` - Integrate LLMs into apps with multi-agent orchestration (Handoff, Supervisor).
- [openai-agents-python](https://github.com/openai/openai-agents-python) ![Stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=social) `Official` `Framework` - Lightweight multi-agent framework with handoffs and orchestration.
- [adk-python](https://github.com/google/adk-python) ![Stars](https://img.shields.io/github/stars/google/adk-python?style=social) `Official` `Framework` `Research` `Infra` - Google's code-first Python toolkit for building multi-agent systems.
- [camel](https://github.com/camel-ai/camel) ![Stars](https://img.shields.io/github/stars/camel-ai/camel?style=social) `Framework` - Multi-agent framework with role-based agent orchestration.
- [swarms](https://github.com/kyegomez/swarms) ![Stars](https://img.shields.io/github/stars/kyegomez/swarms?style=social) `Framework` - Enterprise-grade production-ready multi-agent orchestration framework.
- [sdk-python](https://github.com/strands-agents/sdk-python) ![Stars](https://img.shields.io/github/stars/strands-agents/sdk-python?style=social) `Framework` `Infra` - Model-driven approach to building AI agents with multi-agent patterns.

</details>

### Worker Agents

<details>
<summary><b>Worker Agents</b> — Task execution, parallel processing, and distributed agents</summary>

- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) ![Stars](https://img.shields.io/github/stars/FoundationAgents/MetaGPT?style=social) `Framework` - Multi-agent framework assigning specialist worker roles (PM, Architect, Engineer, QA).
- [ChatDev](https://github.com/OpenBMB/ChatDev) ![Stars](https://img.shields.io/github/stars/OpenBMB/ChatDev?style=social) `Framework` - Multi-agent collaboration with specialist roles (CEO, CTO, Programmer, Tester, Designer).
- [agentscope](https://github.com/agentscope-ai/agentscope) ![Stars](https://img.shields.io/github/stars/agentscope-ai/agentscope?style=social) `Framework` `Research` - Build and run multi-agent systems with distributed agents and customizable skills.
- [AgentVerse](https://github.com/OpenBMB/AgentVerse) ![Stars](https://img.shields.io/github/stars/OpenBMB/AgentVerse?style=social) `Framework` `Infra` - Deploy multiple LLM-based agents with different specializations for task-solving.
- [swarmclaw](https://github.com/swarmclawai/swarmclaw) ![Stars](https://img.shields.io/github/stars/swarmclawai/swarmclaw?style=social) `Framework` `Infra` - Self-hosted multi-agent runtime with delegation, schedules, MCP tools, and durable memory.
- [agentUniverse](https://github.com/agentuniverse-ai/agentUniverse) ![Stars](https://img.shields.io/github/stars/agentuniverse-ai/agentUniverse?style=social) `Framework` - Ant Group multi-agent framework with PEER pattern for plan, execute, express, review.
- [llmling-agent](https://github.com/phil65/llmling-agent) ![Stars](https://img.shields.io/github/stars/phil65/llmling-agent?style=social) `Framework` - YAML-configured multi-agent pools with MCP and ACP support.
- [cli-agent-orchestrator](https://github.com/awslabs/cli-agent-orchestrator) ![Stars](https://img.shields.io/github/stars/awslabs/cli-agent-orchestrator?style=social) `Official` `Framework` - Supervisor-worker orchestration for multiple CLI coding agents in tmux.
- [multi-agent-system](https://github.com/versionHQ/multi-agent-system) ![Stars](https://img.shields.io/github/stars/versionHQ/multi-agent-system?style=social) `Framework` `Research` - Autonomous agent networks for multi-step task automation.
- [EggAI](https://github.com/eggai-tech/EggAI) ![Stars](https://img.shields.io/github/stars/eggai-tech/EggAI?style=social) `Framework` - Async-first meta framework for distributed enterprise multi-agent systems.

</details>

### Reviewer Agents

<details>
<summary><b>Reviewer Agents</b> — Code review, quality assurance, and critic agents</summary>

- [pr-agent](https://github.com/The-PR-Agent/pr-agent) ![Stars](https://img.shields.io/github/stars/The-PR-Agent/pr-agent?style=social) `Framework` - Open-source AI PR review agent with automated code review and improvement suggestions.
- [agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) ![Stars](https://img.shields.io/github/stars/ComposioHQ/agent-orchestrator?style=social) `Official` `Framework` - Parallel coding agents with autonomous CI fixes, merge conflict handling, and code reviews.
- [shippie](https://github.com/mattzcarey/shippie) ![Stars](https://img.shields.io/github/stars/mattzcarey/shippie?style=social) `Framework` - Extendable code review and QA agent for shipping quality code.
- [ai-devkit](https://github.com/codeaholicguy/ai-devkit) ![Stars](https://img.shields.io/github/stars/codeaholicguy/ai-devkit?style=social) `Framework` - AI coding agents with repeatable engineering workflow including planning, memory, and review.
- [claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) ![Stars](https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=social) `Framework` `Example` - Claude Code template with multi-agent review, quality gates, and adversarial QA.
- [sashiko](https://github.com/sashiko-dev/sashiko) ![Stars](https://img.shields.io/github/stars/sashiko-dev/sashiko?style=social) `Framework` - LLM-powered code review agent for Linux Kernel patches.
- [awesome-reviewers](https://github.com/baz-scm/awesome-reviewers) ![Stars](https://img.shields.io/github/stars/baz-scm/awesome-reviewers?style=social) `Framework` `Research` - Curated collection of reviewer agent system prompts.
- [metaswarm](https://github.com/dsifry/metaswarm) ![Stars](https://img.shields.io/github/stars/dsifry/metaswarm?style=social) `Framework` - Multi-agent SDLC framework with adversarial review gates and PR shepherding.
- [Agent-Wiz](https://github.com/Repello-AI/Agent-Wiz) ![Stars](https://img.shields.io/github/stars/Repello-AI/Agent-Wiz?style=social) `Framework` `Infra` - CLI for threat modeling and reviewing AI agents built with popular frameworks.
- [Snif](https://github.com/AssahBismarkabah/Snif) ![Stars](https://img.shields.io/github/stars/AssahBismarkabah/Snif?style=social) `Framework` - Open-source AI code review agent for context-aware large repositories.

</details>

### Specialist Skills

<details>
<summary><b>Specialist Skills</b> — Domain-specific and expert agents</summary>

- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) ![Stars](https://img.shields.io/github/stars/FoundationAgents/MetaGPT?style=social) `Framework` - Multi-agent framework with specialist roles (PM, Architect, Engineer, QA).
- [ChatDev](https://github.com/OpenBMB/ChatDev) ![Stars](https://img.shields.io/github/stars/OpenBMB/ChatDev?style=social) `Framework` - Agents take specialist roles (CEO, CTO, Programmer, Tester, Art Designer).
- [agentscope](https://github.com/agentscope-ai/agentscope) ![Stars](https://img.shields.io/github/stars/agentscope-ai/agentscope?style=social) `Framework` `Research` - Distributed specialist agents with customizable skills.
- [AgentVerse](https://github.com/OpenBMB/AgentVerse) ![Stars](https://img.shields.io/github/stars/OpenBMB/AgentVerse?style=social) `Framework` `Infra` - Deploy agents with different specializations for task-solving and simulation.
- [camel](https://github.com/camel-ai/camel) ![Stars](https://img.shields.io/github/stars/camel-ai/camel?style=social) `Framework` - Role-playing specialist agents in multi-agent framework.
- [AutoGen](https://github.com/microsoft/autogen) ![Stars](https://img.shields.io/github/stars/microsoft/autogen?style=social) `Official` `Framework` `Infra` - Multi-agent framework with specialist assistant, user proxy, critic, and tool agents.
- [crewAI](https://github.com/crewAIInc/crewAI) ![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=social) `Official` `Framework` - Role-based autonomous agents with specialist crews and task delegation.
- [agentUniverse](https://github.com/agentuniverse-ai/agentUniverse) ![Stars](https://img.shields.io/github/stars/agentuniverse-ai/agentUniverse?style=social) `Framework` - Domain-expert agents and collaborative patterns for enterprise applications.
- [metaswarm](https://github.com/dsifry/metaswarm) ![Stars](https://img.shields.io/github/stars/dsifry/metaswarm?style=social) `Framework` `Research` `Infra` - Specialist agent personas for research, architecture, coding, security, and PR work.
- [superagent](https://github.com/homanp/superagent) ![Stars](https://img.shields.io/github/stars/homanp/superagent?style=social) `Framework` - Framework for creating production AI assistants with domain-specific tools.

</details>

### Shared Memory Bus

<details>
<summary><b>Shared Memory Bus</b> — Communication, message passing, and shared memory for multi-agent systems</summary>

- [omem](https://github.com/ourmem/omem) ![Stars](https://img.shields.io/github/stars/ourmem/omem?style=social) `Framework` `Infra` - Shared Memory That Never Forgets — persistent memory with Space-based sharing across agents and teams.
- [eion](https://github.com/eiondb/eion) ![Stars](https://img.shields.io/github/stars/eiondb/eion?style=social) `Framework` `Infra` - Shared Memory Storage for Multi-Agent Systems.
- [stash](https://github.com/Fergana-Labs/stash) ![Stars](https://img.shields.io/github/stars/Fergana-Labs/stash?style=social) `Framework` `Infra` - Shared memory for your team's coding agents.
- [memX](https://github.com/MehulG/memX) ![Stars](https://img.shields.io/github/stars/MehulG/memX?style=social) `Framework` `Infra` - Real-time shared memory layer for multi-agent LLM systems.
- [llegos](https://github.com/CyrusNuevoDia/llegos) ![Stars](https://img.shields.io/github/stars/CyrusNuevoDia/llegos?style=social) `Framework` `Infra` - Strongly typed Python DSL for message passing multi-agent systems.
- [ALMA-memory](https://github.com/RBKunnela/ALMA-memory) ![Stars](https://img.shields.io/github/stars/RBKunnela/ALMA-memory?style=social) `Framework` `Infra` - Persistent memory for AI agents with scoped learning and multi-agent sharing.
- [mem0](https://github.com/mem0ai/mem0) ![Stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social) `Official` `Framework` `Infra` - Universal memory layer for AI agents across apps, tools, and sessions.
- [zep](https://github.com/getzep/zep) ![Stars](https://img.shields.io/github/stars/getzep/zep?style=social) `Official` `Framework` `Example` `Infra` - Memory server and knowledge graph for AI assistants and agent applications.
- [AutoGen](https://github.com/microsoft/autogen) ![Stars](https://img.shields.io/github/stars/microsoft/autogen?style=social) `Official` `Framework` `Infra` - Multi-agent framework with conversational message passing between agents.
- [LangGraph](https://github.com/langchain-ai/langgraph) ![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social) `Official` `Framework` `Infra` - Shared graph state, checkpoints, and stores for coordinated multi-agent workflows.

</details>

---

## 06. Infrastructure

### LangGraph

<details>
<summary><b>LangGraph</b> — Stateful multi-actor agent orchestration on LangChain</summary>

- [langchain](https://github.com/langchain-ai/langchain) ![Stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=social) `Official` `Framework` `Infra` - The agent engineering platform (LangGraph is a core sub-project).
- [deer-flow](https://github.com/bytedance/deer-flow) ![Stars](https://img.shields.io/github/stars/bytedance/deer-flow?style=social) `Framework` `Research` `Infra` - ByteDance's open-source SuperAgent harness built on LangGraph.
- [langgraph](https://github.com/langchain-ai/langgraph) ![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social) `Official` `Framework` `Infra` - Official LangGraph library for stateful multi-actor agent orchestration.
- [deepagents](https://github.com/langchain-ai/deepagents) ![Stars](https://img.shields.io/github/stars/langchain-ai/deepagents?style=social) `Official` `Framework` `Infra` - Batteries-included agent harness built on top of LangGraph.
- [GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) ![Stars](https://img.shields.io/github/stars/NirDiamant/GenAI_Agents?style=social) `Official` `Framework` `Example` `Infra` - 50+ tutorials and implementations for Generative AI Agent techniques.
- [agents-towards-production](https://github.com/NirDiamant/agents-towards-production) ![Stars](https://img.shields.io/github/stars/NirDiamant/agents-towards-production?style=social) `Official` `Framework` `Example` `Infra` - End-to-end tutorials for building production-grade GenAI agents.
- [gemini-fullstack-langgraph-quickstart](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart) ![Stars](https://img.shields.io/github/stars/google-gemini/gemini-fullstack-langgraph-quickstart?style=social) `Official` `Framework` `Example` `Infra` - Fullstack agents using Gemini 2.5 and LangGraph.
- [SurfSense](https://github.com/MODSetter/SurfSense) ![Stars](https://img.shields.io/github/stars/MODSetter/SurfSense?style=social) `Framework` `Example` `Infra` - Open-source privacy-focused alternative to NotebookLM, built with LangGraph.
- [langgraph-supervisor-py](https://github.com/langchain-ai/langgraph-supervisor-py) ![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph-supervisor-py?style=social) `Official` `Framework` `Infra` - LangGraph library for hierarchical supervisor-style multi-agent systems.
- [langgraph-swarm-py](https://github.com/langchain-ai/langgraph-swarm-py) ![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph-swarm-py?style=social) `Official` `Framework` `Infra` - Swarm-style multi-agent handoff library built on LangGraph.

</details>

### CrewAI

<details>
<summary><b>CrewAI</b> — Role-playing autonomous AI agent orchestration</summary>

- [crewAI](https://github.com/crewAIInc/crewAI) ![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=social) `Official` `Framework` `Infra` - Framework for orchestrating role-playing, autonomous AI agents.
- [crewAI-examples](https://github.com/crewAIInc/crewAI-examples) ![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI-examples?style=social) `Official` `Framework` `Example` `Infra` `Archived Classic` - Official collection of examples for CrewAI workflows.
- [crewAI-tools](https://github.com/crewAIInc/crewAI-tools) ![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI-tools?style=social) `Official` `Framework` `Infra` `Archived Classic` - Official tools repository to extend CrewAI agents.
- [CrewAI-Studio](https://github.com/strnad/CrewAI-Studio) ![Stars](https://img.shields.io/github/stars/strnad/CrewAI-Studio?style=social) `Framework` `Infra` - User-friendly GUI for managing and running CrewAI agents.
- [full-stack-ai-agent-template](https://github.com/vstorm-co/full-stack-ai-agent-template) ![Stars](https://img.shields.io/github/stars/vstorm-co/full-stack-ai-agent-template?style=social) `Framework` `Example` `Research` `Infra` - Full-stack AI app generator (FastAPI + Next.js) with CrewAI integration.
- [awesome-crewai](https://github.com/crewAIInc/awesome-crewai) ![Stars](https://img.shields.io/github/stars/crewAIInc/awesome-crewai?style=social) `Official` `Framework` `Research` `Infra` - Curated collection of open-source projects built with CrewAI.
- [crewAI-quickstarts](https://github.com/crewAIInc/crewAI-quickstarts) ![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI-quickstarts?style=social) `Official` `Framework` `Example` `Infra` - Official quickstarts and feature demos for learning CrewAI hands-on.
- [marketplace-crew-template](https://github.com/crewAIInc/marketplace-crew-template) ![Stars](https://img.shields.io/github/stars/crewAIInc/marketplace-crew-template?style=social) `Official` `Framework` `Example` `Infra` - Template for building and submitting CrewAI marketplace crews.
- [companies-powered-by-crewai](https://github.com/crewAIInc/companies-powered-by-crewai) ![Stars](https://img.shields.io/github/stars/crewAIInc/companies-powered-by-crewai?style=social) `Official` `Framework` `Example` `Infra` - Official showcase of companies and platforms using CrewAI in production workflows.
- [template_conversational_example](https://github.com/crewAIInc/template_conversational_example) ![Stars](https://img.shields.io/github/stars/crewAIInc/template_conversational_example?style=social) `Official` `Framework` `Example` `Infra` - Official conversational crew template for CrewAI deployments.

</details>

### OpenAI Agents SDK

<details>
<summary><b>OpenAI Agents SDK</b> — Official OpenAI multi-agent framework</summary>

- [openai-agents-python](https://github.com/openai/openai-agents-python) ![Stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=social) `Official` `Framework` `Infra` - Lightweight, powerful framework for multi-agent workflows (Python).
- [swarm](https://github.com/openai/swarm) ![Stars](https://img.shields.io/github/stars/openai/swarm?style=social) `Official` `Framework` `Infra` - Educational framework exploring lightweight multi-agent orchestration.
- [openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) ![Stars](https://img.shields.io/github/stars/openai/openai-cs-agents-demo?style=social) `Official` `Framework` `Example` `Infra` - Customer service demo with OpenAI Agents SDK.
- [openai-agents-js](https://github.com/openai/openai-agents-js) ![Stars](https://img.shields.io/github/stars/openai/openai-agents-js?style=social) `Official` `Framework` `Infra` - Official JS/TS SDK for multi-agent workflows and voice agents.
- [learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) ![Stars](https://img.shields.io/github/stars/panaversity/learn-agentic-ai?style=social) `Official` `Framework` `Infra` - Learn Agentic AI using OpenAI Agents SDK, MCP, A2A, and Kubernetes.
- [agents-deep-research](https://github.com/qx-labs/agents-deep-research) ![Stars](https://img.shields.io/github/stars/qx-labs/agents-deep-research?style=social) `Official` `Framework` `Research` `Infra` - Iterative deep research implementation using OpenAI Agents SDK.
- [openai-realtime-agents](https://github.com/openai/openai-realtime-agents) ![Stars](https://img.shields.io/github/stars/openai/openai-realtime-agents?style=social) `Official` `Framework` `Example` `Infra` - OpenAI demo patterns for realtime voice agents and handoffs.
- [openai-guardrails-python](https://github.com/openai/openai-guardrails-python) ![Stars](https://img.shields.io/github/stars/openai/openai-guardrails-python?style=social) `Official` `Framework` `Infra` - OpenAI Guardrails package with Agents SDK integration.
- [glean-agent-toolkit](https://github.com/gleanwork/glean-agent-toolkit) ![Stars](https://img.shields.io/github/stars/gleanwork/glean-agent-toolkit?style=social) `Official` `Framework` `Example` `Infra` - Enterprise tool adapters with examples for OpenAI Agents SDK.
- [OpenAI-Agents-SDK](https://github.com/shahidali54/OpenAI-Agents-SDK) ![Stars](https://img.shields.io/github/stars/shahidali54/OpenAI-Agents-SDK?style=social) `Official` `Framework` `Example` `Infra` - Learning repository with practical OpenAI Agents SDK examples and patterns.

</details>

### MCP

<details>
<summary><b>MCP (Model Context Protocol)</b> — Standard protocol for LLM-tool integration</summary>

- [servers](https://github.com/modelcontextprotocol/servers) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=social) `Official` `Infra` - Official Model Context Protocol reference server implementations.
- [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) ![Stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=social) `Infra` - Chrome DevTools for coding agents via MCP.
- [playwright-mcp](https://github.com/microsoft/playwright-mcp) ![Stars](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=social) `Official` `Infra` - Playwright MCP server — browser automation for AI agents.
- [fastmcp](https://github.com/PrefectHQ/fastmcp) ![Stars](https://img.shields.io/github/stars/PrefectHQ/fastmcp?style=social) `Framework` `Infra` - The fast, Pythonic way to build MCP servers and clients.
- [python-sdk](https://github.com/modelcontextprotocol/python-sdk) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/python-sdk?style=social) `Official` `Framework` `Infra` - Official Python SDK for MCP servers and clients.
- [typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/typescript-sdk?style=social) `Official` `Framework` `Infra` - Official TypeScript SDK for MCP servers and clients.
- [fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) ![Stars](https://img.shields.io/github/stars/tadata-org/fastapi_mcp?style=social) `Infra` - Expose FastAPI endpoints as MCP tools with Auth.
- [mcp-go](https://github.com/mark3labs/mcp-go) ![Stars](https://img.shields.io/github/stars/mark3labs/mcp-go?style=social) `Infra` - Go implementation of the Model Context Protocol.
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) ![Stars](https://img.shields.io/github/stars/lastmile-ai/mcp-agent?style=social) `Framework` `Infra` - Build effective agents using MCP and workflow patterns.
- [modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) ![Stars](https://img.shields.io/github/stars/modelcontextprotocol/modelcontextprotocol?style=social) `Official` `Infra` - Specification and documentation for MCP.

</details>

### Docker

<details>
<summary><b>Docker</b> — Containerized agent deployment and management</summary>

- [dify](https://github.com/langgenius/dify) ![Stars](https://img.shields.io/github/stars/langgenius/dify?style=social) `Framework` `Infra` - Production-ready agent platform with Docker-first deployment (docker-compose).
- [OpenHands](https://github.com/OpenHands/OpenHands) ![Stars](https://img.shields.io/github/stars/OpenHands/OpenHands?style=social) `Framework` `Infra` - AI-driven development platform running agents inside Docker sandbox containers.
- [gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) ![Stars](https://img.shields.io/github/stars/Pythagora-io/gpt-pilot?style=social) `Infra` - AI developer using Docker containers for isolated code execution and testing.
- [agent-zero](https://github.com/agent0ai/agent-zero) ![Stars](https://img.shields.io/github/stars/agent0ai/agent-zero?style=social) `Framework` `Infra` - Docker-based multi-agent system with containerized tool execution.
- [text-generation-inference](https://github.com/huggingface/text-generation-inference) ![Stars](https://img.shields.io/github/stars/huggingface/text-generation-inference?style=social) `Official` `Infra` `Archived Classic` - Docker-containerized LLM serving infrastructure for agent backends.
- [llama_deploy](https://github.com/run-llama/llama_deploy) ![Stars](https://img.shields.io/github/stars/run-llama/llama_deploy?style=social) `Official` `Framework` `Infra` - Deploy agentic workflows to production with container-aware deployment.
- [Flowise](https://github.com/FlowiseAI/Flowise) ![Stars](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=social) `Framework` `Research` `Infra` - Low-code LLM app and agent builder with Docker-based self-hosting.
- [coze-studio](https://github.com/coze-dev/coze-studio) ![Stars](https://img.shields.io/github/stars/coze-dev/coze-studio?style=social) `Framework` `Infra` - Open-source AI agent development platform with Docker Compose deployment.
- [n8n](https://github.com/n8n-io/n8n) ![Stars](https://img.shields.io/github/stars/n8n-io/n8n?style=social) `Framework` `Infra` - Workflow automation platform with AI agent nodes and Docker deployment.
- [Agno](https://github.com/agno-agi/agno) ![Stars](https://img.shields.io/github/stars/agno-agi/agno?style=social) `Framework` `Example` `Infra` - Agent framework with Docker examples for deploying agent applications.

</details>

### Kubernetes

<details>
<summary><b>Kubernetes</b> — Scalable agent orchestration on K8s</summary>

- [k8sgpt](https://github.com/k8sgpt-ai/k8sgpt) ![Stars](https://img.shields.io/github/stars/k8sgpt-ai/k8sgpt?style=social) `Framework` `Infra` - Giving Kubernetes Superpowers to everyone — AI-powered K8s diagnostics and SRE.
- [kubectl-ai](https://github.com/GoogleCloudPlatform/kubectl-ai) ![Stars](https://img.shields.io/github/stars/GoogleCloudPlatform/kubectl-ai?style=social) `Official` `Framework` `Infra` - AI powered Kubernetes Assistant — natural language to kubectl via LLM agents.
- [kagent](https://github.com/kagent-dev/kagent) ![Stars](https://img.shields.io/github/stars/kagent-dev/kagent?style=social) `Framework` `Infra` - Cloud Native Agentic AI — run and orchestrate AI agents on Kubernetes.
- [dstack](https://github.com/dstackai/dstack) ![Stars](https://img.shields.io/github/stars/dstackai/dstack?style=social) `Framework` `Infra` - Vendor-agnostic orchestration for AI training, inference, and agentic workloads on K8s.
- [kubeai](https://github.com/kubeai-project/kubeai) ![Stars](https://img.shields.io/github/stars/kubeai-project/kubeai?style=social) `Framework` `Infra` - AI Inference Operator for Kubernetes — easiest way to serve ML models in production.
- [kubectl-ai](https://github.com/sozercan/kubectl-ai) ![Stars](https://img.shields.io/github/stars/sozercan/kubectl-ai?style=social) `Framework` `Infra` - Kubectl plugin to create manifests with LLMs — AI-generated K8s resources.
- [k8sgpt-operator](https://github.com/k8sgpt-ai/k8sgpt-operator) ![Stars](https://img.shields.io/github/stars/k8sgpt-ai/k8sgpt-operator?style=social) `Framework` `Infra` - Automatic SRE Superpowers within your Kubernetes cluster — operator for k8sgpt.
- [arcadia](https://github.com/kubeagi/arcadia) ![Stars](https://img.shields.io/github/stars/kubeagi/arcadia?style=social) `Framework` `Research` `Infra` - Diverse, simple, and secure all-in-one LLMOps platform on Kubernetes.
- [kubeflow](https://github.com/kubeflow/kubeflow) ![Stars](https://img.shields.io/github/stars/kubeflow/kubeflow?style=social) `Framework` `Example` `Infra` - Cloud-native ML toolkit for running AI workloads on Kubernetes.
- [kserve](https://github.com/kserve/kserve) ![Stars](https://img.shields.io/github/stars/kserve/kserve?style=social) `Framework` `Infra` - Standard Kubernetes inference platform for model serving behind agents.

**Related K8s infrastructure for AI serving:** [kubeflow](https://github.com/kubeflow/kubeflow) (ML Toolkit for K8s), [kserve](https://github.com/kserve/kserve) (Standardized AI Inference on K8s), [llm-d](https://github.com/llm-d/llm-d) (State-of-the-art LLM inference on K8s).

</details>

---

## 07. Observability

### Logging

<details>
<summary><b>Logging</b> — LLM and agent logging, monitoring, and observability platforms</summary>

- [langfuse](https://github.com/langfuse/langfuse) ![Stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social) `Official` `Framework` `Example` `Research` `Infra` - Open source LLM engineering platform: observability, metrics, evals, prompt management.
- [mlflow](https://github.com/mlflow/mlflow) ![Stars](https://img.shields.io/github/stars/mlflow/mlflow?style=social) `Framework` `Research` `Infra` - Open source AI engineering platform for agents, LLMs, and ML models with tracing and cost control.
- [opik](https://github.com/comet-ml/opik) ![Stars](https://img.shields.io/github/stars/comet-ml/opik?style=social) `Framework` `Example` `Research` `Infra` - Debug, evaluate, and monitor LLM applications and agentic workflows.
- [openobserve](https://github.com/openobserve/openobserve) ![Stars](https://img.shields.io/github/stars/openobserve/openobserve?style=social) `Official` `Framework` `Research` `Infra` - Open source observability for logs, metrics, traces, and LLM observability.
- [RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) ![Stars](https://img.shields.io/github/stars/raga-ai-hub/RagaAI-Catalyst?style=social) `Framework` `Infra` - Agent AI Observability: tracing, debugging multi-agentic systems with timeline and execution graph.
- [phoenix](https://github.com/Arize-ai/phoenix) ![Stars](https://img.shields.io/github/stars/Arize-ai/phoenix?style=social) `Framework` `Research` `Infra` - AI Observability and Evaluation: tracing, evaluation, and debugging for LLM applications.
- [openllmetry](https://github.com/traceloop/openllmetry) ![Stars](https://img.shields.io/github/stars/traceloop/openllmetry?style=social) `Official` `Framework` `Research` `Infra` - Open-source OpenTelemetry-native observability for GenAI/LLM applications.
- [helicone](https://github.com/Helicone/helicone) ![Stars](https://img.shields.io/github/stars/Helicone/helicone?style=social) `Official` `Framework` `Example` `Research` `Infra` - Open source LLM observability — one line of code to monitor, evaluate, and experiment.
- [agentops](https://github.com/AgentOps-AI/agentops) ![Stars](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=social) `Official` `Framework` `Research` `Infra` - Python SDK for AI agent monitoring, LLM cost tracking, and benchmarking.
- [logfire](https://github.com/pydantic/logfire) ![Stars](https://img.shields.io/github/stars/pydantic/logfire?style=social) `Official` `Framework` `Research` `Infra` - AI observability platform for production LLM and agent systems (Pydantic team).

</details>

### Tracing

<details>
<summary><b>Tracing</b> — LLM telemetry, distributed tracing, and request tracking</summary>

- [langfuse](https://github.com/langfuse/langfuse) ![Stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social) `Official` `Framework` `Example` `Research` `Infra` - LLM engineering platform with comprehensive tracing (OpenTelemetry, Langchain, OpenAI SDK).
- [opik](https://github.com/comet-ml/opik) ![Stars](https://img.shields.io/github/stars/comet-ml/opik?style=social) `Framework` `Example` `Research` `Infra` - Comprehensive tracing and automated evaluations for LLM/agent workflows.
- [gateway](https://github.com/Portkey-AI/gateway) ![Stars](https://img.shields.io/github/stars/Portkey-AI/gateway?style=social) `Official` `Framework` `Infra` - Blazing fast AI Gateway with integrated guardrails, routing to 1600+ LLMs.
- [phoenix](https://github.com/Arize-ai/phoenix) ![Stars](https://img.shields.io/github/stars/Arize-ai/phoenix?style=social) `Framework` `Research` `Infra` - Tracing, evaluation, and experimentation for LLM/agent workflows.
- [openllmetry](https://github.com/traceloop/openllmetry) ![Stars](https://img.shields.io/github/stars/traceloop/openllmetry?style=social) `Official` `Research` `Infra` - OpenTelemetry-native drop-in instrumentation for any LLM provider.
- [helicone](https://github.com/Helicone/helicone) ![Stars](https://img.shields.io/github/stars/Helicone/helicone?style=social) `Official` `Framework` `Example` `Research` `Infra` - LLM observability with one-line monitoring and evaluation.
- [agenta](https://github.com/Agenta-AI/agenta) ![Stars](https://img.shields.io/github/stars/Agenta-AI/agenta?style=social) `Framework` `Example` `Research` `Infra` - LLMOps platform: prompt playground, management, evaluation, and observability.
- [openlit](https://github.com/openlit/openlit) ![Stars](https://img.shields.io/github/stars/openlit/openlit?style=social) `Official` `Research` `Infra` - OpenTelemetry-native LLM observability, GPU monitoring, guardrails, evaluations.
- [weave](https://github.com/wandb/weave) ![Stars](https://img.shields.io/github/stars/wandb/weave?style=social) `Official` `Framework` `Research` `Infra` - Weights & Biases toolkit for tracing, evaluation, and monitoring LLM apps.
- [langsmith-sdk](https://github.com/langchain-ai/langsmith-sdk) ![Stars](https://img.shields.io/github/stars/langchain-ai/langsmith-sdk?style=social) `Official` `Framework` `Research` `Infra` - LangSmith Client SDK for tracing, evaluation, and debugging.

</details>

### Evaluation

<details>
<summary><b>Evaluation</b> — LLM and agent benchmarking, testing, and metrics</summary>

- [promptfoo](https://github.com/promptfoo/promptfoo) ![Stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social) `Framework` `Research` `Infra` - Test prompts, agents, and RAGs. Red teaming, vulnerability scanning for AI.
- [evals](https://github.com/openai/evals) ![Stars](https://img.shields.io/github/stars/openai/evals?style=social) `Official` `Framework` `Research` `Infra` - Framework for evaluating LLMs and LLM systems with open-source benchmark registry.
- [deepeval](https://github.com/confident-ai/deepeval) ![Stars](https://img.shields.io/github/stars/confident-ai/deepeval?style=social) `Framework` `Research` `Infra` - The LLM Evaluation Framework — metrics, datasets, and integrations.
- [ragas](https://github.com/explodinggradients/ragas) ![Stars](https://img.shields.io/github/stars/explodinggradients/ragas?style=social) `Framework` `Research` `Infra` - Framework for evaluating RAG pipelines and LLM applications.
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) ![Stars](https://img.shields.io/github/stars/EleutherAI/lm-evaluation-harness?style=social) `Official` `Framework` `Research` `Infra` - Few-shot evaluation framework for language models (200+ tasks).
- [opencompass](https://github.com/open-compass/opencompass) ![Stars](https://img.shields.io/github/stars/open-compass/opencompass?style=social) `Official` `Framework` `Research` `Infra` - LLM evaluation platform supporting 100+ datasets across major models.
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) ![Stars](https://img.shields.io/github/stars/SWE-bench/SWE-bench?style=social) `Official` `Framework` `Research` `Infra` - Can LLMs resolve real GitHub issues? Benchmark for coding agent evaluation.
- [AgentBench](https://github.com/THUDM/AgentBench) ![Stars](https://img.shields.io/github/stars/THUDM/AgentBench?style=social) `Official` `Research` `Infra` - Comprehensive benchmark to evaluate LLMs as Agents (ICLR'24).
- [langwatch](https://github.com/langwatch/langwatch) ![Stars](https://img.shields.io/github/stars/langwatch/langwatch?style=social) `Framework` `Research` `Infra` - Platform for LLM evaluations and AI agent testing with observability.
- [agentevals](https://github.com/langchain-ai/agentevals) ![Stars](https://img.shields.io/github/stars/langchain-ai/agentevals?style=social) `Official` `Research` `Infra` - Ready-made evaluators for agent trajectories and intermediate steps.

</details>

### Hallucination Detection

<details>
<summary><b>Hallucination Detection</b> — Fact checking, grounding, and hallucination mitigation</summary>

- [langextract](https://github.com/google/langextract) ![Stars](https://img.shields.io/github/stars/google/langextract?style=social) `Official` `Research` `Infra` - Extract structured information with precise source grounding and attribution.
- [git-mcp](https://github.com/idosal/git-mcp) ![Stars](https://img.shields.io/github/stars/idosal/git-mcp?style=social) `Research` `Infra` - Put an end to code hallucinations. Free MCP server for grounding LLM coding agents.
- [hallucination-leaderboard](https://github.com/vectara/hallucination-leaderboard) ![Stars](https://img.shields.io/github/stars/vectara/hallucination-leaderboard?style=social) `Research` `Infra` - Leaderboard comparing LLM hallucination rates when summarizing documents.
- [WikiChat](https://github.com/stanford-oval/WikiChat) ![Stars](https://img.shields.io/github/stars/stanford-oval/WikiChat?style=social) `Official` `Research` `Infra` - Improved RAG that stops LLM hallucination by retrieving from a corpus (Stanford).
- [uqlm](https://github.com/cvs-health/uqlm) ![Stars](https://img.shields.io/github/stars/cvs-health/uqlm?style=social) `Framework` `Research` `Infra` - Uncertainty Quantification for Language Models — UQ-based hallucination detection.
- [awesome-hallucination-detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) ![Stars](https://img.shields.io/github/stars/EdinburghNLP/awesome-hallucination-detection?style=social) `Research` `Infra` - Curated list of papers on hallucination detection in LLMs.
- [llm-hallucination-survey](https://github.com/HillZhang1999/llm-hallucination-survey) ![Stars](https://img.shields.io/github/stars/HillZhang1999/llm-hallucination-survey?style=social) `Research` `Infra` - Reading list and survey on hallucination in LLMs.
- [dingo](https://github.com/MigoXLab/dingo) ![Stars](https://img.shields.io/github/stars/MigoXLab/dingo?style=social) `Research` `Infra` - Comprehensive AI quality evaluation tool covering hallucination detection.
- [Woodpecker](https://github.com/VITA-MLLM/Woodpecker) ![Stars](https://img.shields.io/github/stars/VITA-MLLM/Woodpecker?style=social) `Research` `Infra` - Hallucination correction for multimodal large language models.
- [LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect) ![Stars](https://img.shields.io/github/stars/KRLabsOrg/LettuceDetect?style=social) `Framework` `Research` `Infra` - Lightweight hallucination detection framework for RAG applications.

</details>

### Cost Monitoring

<details>
<summary><b>Cost Monitoring</b> — Token usage tracking, spend management, and budget control</summary>

- [langfuse](https://github.com/langfuse/langfuse) ![Stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social) `Official` `Framework` `Example` `Research` `Infra` - LLM engineering platform with built-in cost tracking and metrics.
- [openobserve](https://github.com/openobserve/openobserve) ![Stars](https://img.shields.io/github/stars/openobserve/openobserve?style=social) `Official` `Framework` `Research` `Infra` - Observability platform with LLM cost monitoring (140x lower storage costs).
- [evidently](https://github.com/evidentlyai/evidently) ![Stars](https://img.shields.io/github/stars/evidentlyai/evidently?style=social) `Framework` `Example` `Research` `Infra` - ML and LLM observability with 100+ metrics for evaluation and monitoring.
- [helicone](https://github.com/Helicone/helicone) ![Stars](https://img.shields.io/github/stars/Helicone/helicone?style=social) `Official` `Framework` `Example` `Research` `Infra` - LLM observability with focused cost tracking features.
- [agentops](https://github.com/AgentOps-AI/agentops) ![Stars](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=social) `Official` `Framework` `Research` `Infra` - Python SDK for AI agent monitoring and LLM cost tracking.
- [agenta](https://github.com/Agenta-AI/agenta) ![Stars](https://img.shields.io/github/stars/Agenta-AI/agenta?style=social) `Framework` `Example` `Research` `Infra` - LLMOps platform with LLM cost observability.
- [openlit](https://github.com/openlit/openlit) ![Stars](https://img.shields.io/github/stars/openlit/openlit?style=social) `Official` `Infra` - OpenTelemetry-native LLM observability, GPU monitoring, and cost tracking.
- [langkit](https://github.com/whylabs/langkit) ![Stars](https://img.shields.io/github/stars/whylabs/langkit?style=social) `Framework` `Research` `Infra` - Toolkit for monitoring LLMs — text quality, relevance metrics, sentiment analysis.
- [litellm](https://github.com/BerriAI/litellm) ![Stars](https://img.shields.io/github/stars/BerriAI/litellm?style=social) `Official` `Framework` `Infra` - LLM gateway with spend tracking, budgets, virtual keys, and usage analytics.
- [gateway](https://github.com/Portkey-AI/gateway) ![Stars](https://img.shields.io/github/stars/Portkey-AI/gateway?style=social) `Official` `Framework` `Infra` - AI gateway with logs, analytics, budgets, and provider-level cost controls.

</details>

---

## 08. Security

### Sandboxing

<details>
<summary><b>Sandboxing</b> — Isolated execution environments for AI agent security</summary>

- [daytona](https://github.com/daytonaio/daytona) ![Stars](https://img.shields.io/github/stars/daytonaio/daytona?style=social) `Framework` `Infra` - Secure and elastic infrastructure for running AI-generated code.
- [E2B](https://github.com/e2b-dev/E2B) ![Stars](https://img.shields.io/github/stars/e2b-dev/E2B?style=social) `Official` `Research` `Infra` - Open-source secure sandboxed cloud environment for enterprise-grade AI agents.
- [microsandbox](https://github.com/superradcompany/microsandbox) ![Stars](https://img.shields.io/github/stars/superradcompany/microsandbox?style=social) `Framework` `Infra` - Secure, local and programmable sandboxes for AI agents.
- [sandbox-agent](https://github.com/rivet-dev/sandbox-agent) ![Stars](https://img.shields.io/github/stars/rivet-dev/sandbox-agent?style=social) `Infra` - Run coding agents in sandboxes over HTTP. Supports Claude Code, Codex, OpenCode.
- [desktop](https://github.com/e2b-dev/desktop) ![Stars](https://img.shields.io/github/stars/e2b-dev/desktop?style=social) `Official` `Framework` `Infra` - E2B Desktop Sandbox for secure computer use with graphical environment.
- [llm-sandbox](https://github.com/vndee/llm-sandbox) ![Stars](https://img.shields.io/github/stars/vndee/llm-sandbox?style=social) `Framework` `Infra` - Lightweight and portable LLM sandbox runtime Python library.
- [open-ptc-agent](https://github.com/Chen-zexi/open-ptc-agent) ![Stars](https://img.shields.io/github/stars/Chen-zexi/open-ptc-agent?style=social) `Infra` - Sandboxed code execution with MCP (Programmatic Tool Calling).
- [the-agent-sandbox-taxonomy](https://github.com/kajogo777/the-agent-sandbox-taxonomy) ![Stars](https://img.shields.io/github/stars/kajogo777/the-agent-sandbox-taxonomy?style=social) `Framework` `Research` `Infra` - Open taxonomy and scoring framework for evaluating AI agent sandboxes.
- [agent-sandbox](https://github.com/agent-sandbox/agent-sandbox) ![Stars](https://img.shields.io/github/stars/agent-sandbox/agent-sandbox?style=social) `Infra` - E2B-compatible enterprise sandboxes for AI agents, code, browser, and computer use.
- [sandbox](https://github.com/agent-infra/sandbox) ![Stars](https://img.shields.io/github/stars/agent-infra/sandbox?style=social) `Framework` `Infra` - All-in-one Docker sandbox combining browser, shell, file, MCP, and VS Code Server for agents.

</details>

### Permission Control

<details>
<summary><b>Permission Control</b> — Access control, authorization, and RBAC for AI agents</summary>

- [agentshield](https://github.com/affaan-m/agentshield) ![Stars](https://img.shields.io/github/stars/affaan-m/agentshield?style=social) `Infra` - AI agent security scanner. Detect vulnerabilities in agent configurations, MCP servers, and tool permissions.
- [crust](https://github.com/BakeLens/crust) ![Stars](https://img.shields.io/github/stars/BakeLens/crust?style=social) `Infra` - Open Source AI Agent Security Infrastructure — intercepts and blocks dangerous agent behaviors.
- [aport-agent-guardrails](https://github.com/aporthq/aport-agent-guardrails) ![Stars](https://img.shields.io/github/stars/aporthq/aport-agent-guardrails?style=social) `Framework` `Infra` - Pre-action authorization guardrails for AI agents. Works with OpenAI, Claude Code, LangChain, CrewAI.
- [agent-guardrails](https://github.com/logi-cmd/agent-guardrails) ![Stars](https://img.shields.io/github/stars/logi-cmd/agent-guardrails?style=social) `Infra` - Merge gates and safety checks for AI coding agents via MCP.
- [opa](https://github.com/open-policy-agent/opa) ![Stars](https://img.shields.io/github/stars/open-policy-agent/opa?style=social) `Framework` `Infra` - General-purpose policy engine for declarative authorization and tool permission checks.
- [gatekeeper](https://github.com/open-policy-agent/gatekeeper) ![Stars](https://img.shields.io/github/stars/open-policy-agent/gatekeeper?style=social) `Framework` `Infra` - Kubernetes admission-control policy engine for enforcing deployment permissions.
- [conftest](https://github.com/open-policy-agent/conftest) ![Stars](https://img.shields.io/github/stars/open-policy-agent/conftest?style=social) `Infra` - Test configuration and deployment manifests against Rego permission policies.
- [spicedb](https://github.com/authzed/spicedb) ![Stars](https://img.shields.io/github/stars/authzed/spicedb?style=social) `Framework` `Research` `Infra` - Fine-grained authorization database for application permissions and relationships.
- [cerbos](https://github.com/cerbos/cerbos) ![Stars](https://img.shields.io/github/stars/cerbos/cerbos?style=social) `Infra` - Authorization layer for contextual RBAC and ABAC decisions.
- [arcade-mcp](https://github.com/ArcadeAI/arcade-mcp) ![Stars](https://img.shields.io/github/stars/ArcadeAI/arcade-mcp?style=social) `Official` `Framework` `Infra` - MCP tool framework with OAuth, per-tool scopes, and authorized agent actions.

</details>

### Key Management

<details>
<summary><b>Key Management</b> — API key rotation, secret management, and credential security</summary>

- [keypal](https://github.com/izadoesdev/keypal) ![Stars](https://img.shields.io/github/stars/izadoesdev/keypal?style=social) `Framework` `Infra` - TypeScript library for secure API key management with hashing, expiration, and scopes.
- [forge](https://github.com/TensorBlock/forge) ![Stars](https://img.shields.io/github/stars/TensorBlock/forge?style=social) `Infra` - Self-hosted middleware unifying access to multiple AI providers with encrypted key management.
- [voidllm](https://github.com/voidmind-io/voidllm) ![Stars](https://img.shields.io/github/stars/voidmind-io/voidllm?style=social) `Infra` - Privacy-first LLM proxy with API key management, load balancing, and rate limiting.
- [cligate](https://github.com/codeking-ai/cligate) ![Stars](https://img.shields.io/github/stars/codeking-ai/cligate?style=social) `Infra` - Multi-protocol AI proxy with account pooling and API key management for Claude Code, Codex CLI, Gemini CLI.
- [agentfence](https://github.com/agentfence/agentfence) ![Stars](https://img.shields.io/github/stars/agentfence/agentfence?style=social) `Framework` `Infra` - Automatic AI agent security testing — identifies prompt injection and secret leakage.
- [llm-keypool](https://github.com/piyush-tyagi-13/llm-keypool) ![Stars](https://img.shields.io/github/stars/piyush-tyagi-13/llm-keypool?style=social) `Infra` - Free-tier LLM API key pool with rotation, cooldown handling, and OpenAI-compatible proxy.
- [vault](https://github.com/hashicorp/vault) ![Stars](https://img.shields.io/github/stars/hashicorp/vault?style=social) `Framework` `Infra` - Secrets management and dynamic credential broker for production agent systems.
- [infisical](https://github.com/Infisical/infisical) ![Stars](https://img.shields.io/github/stars/Infisical/infisical?style=social) `Framework` `Infra` - Open-source platform for managing secrets, API keys, and environment configuration.
- [litellm](https://github.com/BerriAI/litellm) ![Stars](https://img.shields.io/github/stars/BerriAI/litellm?style=social) `Official` `Framework` `Infra` - LLM proxy with virtual keys, budgets, rotation, and spend controls.
- [gateway](https://github.com/Portkey-AI/gateway) ![Stars](https://img.shields.io/github/stars/Portkey-AI/gateway?style=social) `Official` `Framework` `Infra` - AI gateway for virtual keys, provider credentials, rate limits, and access policies.

</details>

### Guardrails

<details>
<summary><b>Guardrails</b> — Content safety, input/output filtering, and behavior constraints</summary>

- [guardrails](https://github.com/guardrails-ai/guardrails) ![Stars](https://img.shields.io/github/stars/guardrails-ai/guardrails?style=social) `Infra` - Adding guardrails to large language models.
- [Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) ![Stars](https://img.shields.io/github/stars/NVIDIA-NeMo/Guardrails?style=social) `Framework` `Infra` - NVIDIA NeMo Guardrails — programmable guardrails for LLM-based conversational systems.
- [PurpleLlama](https://github.com/meta-llama/PurpleLlama) ![Stars](https://img.shields.io/github/stars/meta-llama/PurpleLlama?style=social) `Official` `Infra` - Meta's tools to assess and improve LLM security.
- [llm-guard](https://github.com/protectai/llm-guard) ![Stars](https://img.shields.io/github/stars/protectai/llm-guard?style=social) `Official` `Framework` `Infra` - The Security Toolkit for LLM Interactions (Protect AI).
- [rebuff](https://github.com/protectai/rebuff) ![Stars](https://img.shields.io/github/stars/protectai/rebuff?style=social) `Official` `Framework` `Infra` `Archived Classic` - LLM Prompt Injection Detector.
- [modelscan](https://github.com/protectai/modelscan) ![Stars](https://img.shields.io/github/stars/protectai/modelscan?style=social) `Official` `Infra` - Protection against Model Serialization Attacks.
- [openai-guardrails-python](https://github.com/openai/openai-guardrails-python) ![Stars](https://img.shields.io/github/stars/openai/openai-guardrails-python?style=social) `Official` `Infra` - Configurable input/output validation and moderation guardrails for LLM applications.
- [invariant](https://github.com/invariantlabs-ai/invariant) ![Stars](https://img.shields.io/github/stars/invariantlabs-ai/invariant?style=social) `Official` `Infra` - Guardrails for secure and robust agent development using trace-based policies.
- [presidio](https://github.com/microsoft/presidio) ![Stars](https://img.shields.io/github/stars/microsoft/presidio?style=social) `Official` `Framework` `Infra` - PII detection, redaction, masking, and anonymization for privacy guardrails.
- [garak](https://github.com/NVIDIA/garak) ![Stars](https://img.shields.io/github/stars/NVIDIA/garak?style=social) `Official` `Research` `Infra` - LLM vulnerability scanner for testing guardrail coverage and jailbreak resistance.

</details>

### Human-in-the-Loop

<details>
<summary><b>Human-in-the-Loop</b> — Human approval, oversight, and feedback mechanisms</summary>

- [magentic-ui](https://github.com/microsoft/magentic-ui) ![Stars](https://img.shields.io/github/stars/microsoft/magentic-ui?style=social) `Official` `Framework` `Infra` - Experimental human-in-the-loop agent UI for browser and file system tasks with collaborative execution.
- [Observal](https://github.com/BlazeUp-AI/Observal) ![Stars](https://img.shields.io/github/stars/BlazeUp-AI/Observal?style=social) `Official` `Framework` `Example` `Research` `Infra` - Observability and evaluation platform specifically built for human-in-the-loop agents.
- [agent-inbox](https://github.com/langchain-ai/agent-inbox) ![Stars](https://img.shields.io/github/stars/langchain-ai/agent-inbox?style=social) `Official` `Infra` - Inbox-style UX for interacting with human-in-the-loop agents — review and approve agent actions.
- [clawvisor](https://github.com/clawvisor/clawvisor) ![Stars](https://img.shields.io/github/stars/clawvisor/clawvisor?style=social) `Official` `Infra` - Purpose-based authorization gateway for AI agents with human approvals.
- [humanlayer](https://github.com/humanlayer/humanlayer) ![Stars](https://img.shields.io/github/stars/humanlayer/humanlayer?style=social) `Framework` `Infra` - SDK for human approval and feedback in high-stakes agent tool calls.
- [rpi-coordination-template](https://github.com/humanlayer/rpi-coordination-template) ![Stars](https://img.shields.io/github/stars/humanlayer/rpi-coordination-template?style=social) `Framework` `Example` `Infra` - HumanLayer coordination template for applying approval workflows across repositories.
- [langgraph](https://github.com/langchain-ai/langgraph) ![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social) `Official` `Framework` `Infra` - Agent orchestration framework with interrupts and checkpointed HITL workflows.
- [agents-from-scratch-ts](https://github.com/langchain-ai/agents-from-scratch-ts) ![Stars](https://img.shields.io/github/stars/langchain-ai/agents-from-scratch-ts?style=social) `Official` `Framework` `Example` `Infra` - LangGraph TypeScript notebooks covering email agents, memory, and human-in-the-loop.
- [AutoGen](https://github.com/microsoft/autogen) ![Stars](https://img.shields.io/github/stars/microsoft/autogen?style=social) `Official` `Framework` `Infra` - Multi-agent framework with human proxy agents and interactive oversight patterns.
- [crewAI](https://github.com/crewAIInc/crewAI) ![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=social) `Official` `Framework` `Infra` - Agent framework with human input and review hooks for task execution.

**Note:** Major agent frameworks with built-in HITL support include [AutoGen](https://github.com/microsoft/autogen) (HumanProxyAgent), [CrewAI](https://github.com/crewAIInc/crewAI) (human_input tools), and [LangGraph](https://github.com/langchain-ai/langgraph) (interrupt_before/interrupt_after checkpoints).

</details>

---

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) and [selection criteria](SELECTION_CRITERIA.md) first.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
