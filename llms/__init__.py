# llms/__init__.py
from .llms import LLMs as llms
from .openai import OpenAI as openai
from .openai.gpt35turbo import GPT35Turbo as gpt_35_turbo
from .openai.gpt35turbo16k import GPT35Turbo16k as gpt_35_turbo_16k
from .openai.gpt4turbo import GPT4Turbo as gpt_4_turbo
from .openai.gpt4o import GPT4o as gpt_4o
from .openai.gpt4 import GPT4 as gpt_4
from .openai.gpt432k import GPT432k as gpt_4_32k
from .azure import AzureOpenAI as azure
from .azure.gpt35turbo import AzureGPT35Turbo as azure_gpt_35_turbo
from .azure.gpt35turbo16k import AzureGPT35Turbo16k as azure_gpt_35_turbo_16k
from .azure.gpt4turbo import AzureGPT4Turbo as azure_gpt_4_turbo
from .azure.gpt4 import AzureGPT4 as azure_gpt_4
from .azure.gpt432k import AzureGPT432k as azure_gpt_4_32k
from .aws import AWS as aws
from .aws.claude3haiku import Claude3Haiku as claude_3_haiku
from .aws.claude3sonnet import Claude3Sonnet as claude_3_sonnet
from .aws.claude3opus import Claude3Opus as claude_3_opus
from .aws.claude1instant import Claude1Instant as claude_1_instant
from .aws.claude2 import Claude2 as claude_2
from .aws.llama270b import Llama270b as llama2_70b
from .aws.llama38binstruct import Llama38bInstruct as llama3_8b_instruct
from .aws.llama370binstruct import Llama370bInstruct as llama3_70b_instruct
from .aws.mistral7binstruct import Mistral7bInstruct as mistral_7b_instruct
from .aws.mistrallarge import MistralLarge as mistral_large
from .aws.mistralsmall import MistralSmall as mistral_small
from .aws.mixtral8x7binstruct import Mixtral8x7bInstruct as mixtral_8x7b_instruct
from .aws.coherecommand14 import CohereCommand14 as cohere_command_14
from .aws.coherecommandlight14 import CohereCommandLight14 as cohere_command_light_14
#from .aws.coherecommandr import CohereCommandR as coherecommand_r
#from .aws.coherecommandrplus import CohereCommandRPlus as coherecommand_r_plus
from .aws.j2mid import J2Mid as j2_mid
from .aws.j2ultra import J2Ultra as j2_ultra
from .aws.titanlitev1 import TitanLiteV1 as titan_lite_v1
from .aws.titanexpressv1 import TitanExpressV1 as titan_express_v1
from .aws.titanpremierv1 import TitanPremierV1 as titan_premier_v1
from .google import Google as google
from .google.geminipro1 import GeminiPro1 as gemini_pro_1
from .google.geminipro15 import GeminiPro15 as gemini_pro_1_5
from .google.geminiflash15 import GeminiFlash15 as gemini_flash_1_5
from .google.bison import Bison as bison
from .google.bison32k import Bison32k as bison_32k
from .ollama import OllamaLLM as ollama

_all__ = ['llms', 'openai', 'gpt_35_turbo', 'gpt_35_turbo_16k', 'gpt_4_turbo', 'gpt_4o', 'gpt_4', 'gpt_4_32k', 'azure', 'azure_gpt_35_turbo', 'azure_gpt_35_turbo_16k', 'azure_gpt_4_turbo', 'azure_gpt_4', 'azure_gpt_4_32k', 'aws', 'claude_3_haiku', 'claude_3_sonnet', 'claude_3_opus', 'claude_1_instant', 'claude_2', 'llama2_70b', 'llama3_8b_instruct', 'llama3_70b_instruct', 'mistral_7b_instruct', 'mistral_large', 'mistral_small', 'mixtral_8x7b_instruct', 'cohere_command_14', 'cohere_command_light_14', 'j2_mid', 'j2_ultra', 'google', 'gemini_pro_1', 'gemini_pro_1_5', 'gemini_flash_1_5', 'bison', 'bison_32k', 'ollama']
