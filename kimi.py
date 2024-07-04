
from openai import OpenAI
import logging
from typing import Any, Dict, Iterator, List, Mapping, Optional
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models import LLM
from openai import OpenAI


class Kimi(LLM):


    @property
    def _llm_type(self) -> str:
        """Return type of LLM."""
        return "kimillm"

    def _call(self, 
              prompt: str, 
              stop: Optional[List[str]] = None,
              run_manager: Optional[CallbackManagerForLLMRun] = None,
              **kwargs: Any) -> str:

        try:
          
            client = OpenAI(
                api_key="sk-hF6MmoJLUt0xQ9PUBjQ0GJrYf3K2i3GRiXGyUNtBGsEYFKnI",
                base_url="https://api.moonshot.cn/v1",
            )
            completion = client.chat.completions.create(
                model="moonshot-v1-8k",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                
                temperature=0,
            )
            return completion.choices[0].message.content
        except Exception as e:
            logging.error(f"Error in Kimi _call: {e}", exc_info=True)
            raise




