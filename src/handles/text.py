from src.logs.log import logger

"""
rota de text
"""
from src.schema.text import ValidTextRouter
from src.service.orquestration_agent import request_llm, orquestration_model, api_key
from src.service.optimizate_agent import optimizate_model
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import asyncio
router_text = APIRouter(prefix="/text", tags=["text"])

@router_text.post("/")
async def text_orquestration(payload:ValidTextRouter):

    try:

        if (payload.optimizate and payload.optimizate_limit is None) or (payload.optimizate and payload.optimizate_limit is not None 
                                  and payload.optimizate_limit>=len(payload.input.split())):


            options, input =await asyncio.gather(orquestration_model(input=payload.input), optimizate_model(input=payload.input))

        else:

            options = await orquestration_model(input=payload.input)
            input = payload.input


        options = options.split("|")
        model, verbosity = options[0], options[1]
        
        response = await request_llm(input=input, temperature=payload.temperature, 
                               max_token=payload.max_token, prompt=payload.prompt, api_key=api_key, model=model,
                               verbosity=verbosity
                               )
        return JSONResponse(
            status_code=201, 
            content={"output": response, "model": model, "type": "text"}
        )

    except Exception as e:

        return JSONResponse(
            status_code=501, content={"error":e}
        )

