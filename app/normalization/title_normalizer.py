from __future__ import annotations

from openai import AsyncOpenAI

from app.settings import settings


client = AsyncOpenAI(api_key=settings.openai_api_key)


async def normalize_listing_title(raw_title: str) -> str:
    """Placeholder normalization using OpenAI API.

    Replace this with your preferred prompting strategy and schema validation.
    """
    _ = raw_title
    # Example (commented) call:
    # response = await client.responses.create(
    #     model="gpt-4.1-mini",
    #     input=f"Normalize this watch listing title: {raw_title}",
    # )
    # return response.output_text.strip()
    return raw_title.strip()
