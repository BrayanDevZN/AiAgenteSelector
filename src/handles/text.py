from src.logs.log import logger

"""
rota de text
"""
from src.schema.text import ValidTextRouter
from service.agent import request_llm, orquestration_model, api_key



from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
router_text = APIRouter(prefix="/text", tags=["text"])


@router_text.post("/")
async def text_orquestration(payload:ValidTextRouter):

    try:

        model = orquestration_model(input=payload.input)

        response = request_llm(input=payload.input, temperature=payload.temperature, 
                               max_token=payload.max_token, prompt=payload.prompt, api_key=api_key
                               )
        return JSONResponse(
            status_code=201, 
            content={"response": response, "model": model, "type": "text"}
        )

    except Exception as e:

        raise HTTPException(
            detail=e,
            status_code=501
        )


