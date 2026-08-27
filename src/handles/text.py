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
        

        if payload.optimizate and ((not "limit" in payload.optimizate.keys()) or 
                                   (payload.optimizate["limit"]>=len(payload.input))):


            options, input =(await asyncio.gather(orquestration_model(input=payload.input, 
                            verbosity=True if payload.verbosity else False), 
                            optimizate_model(input=payload.input, 
                            verbosity=payload.optimizate["verbosity"])))

        else:

            options = await orquestration_model(input=payload.input, verbosity=True if payload.verbosity else False)
            input = payload.input


        if payload.verbosity:


            options = options.split("|")
            model, verbosity = options[0], options[1]
            
            response = await request_llm(input=input, temperature=payload.temperature, 
                                max_token=payload.max_token, prompt=payload.prompt, api_key=api_key, model=model,
                                verbosity=verbosity
                                )

        else:

            response = await request_llm(
                input=input, temperature=payload.temperature, 
                max_token=payload.max_token, prompt=payload.prompt, api_key=api_key, model=model)

        
        return JSONResponse(
            status_code=201, 
            content={"output": response, "model": model, "type": "text"}
        )

    except Exception as e:

        return JSONResponse(
            status_code=501, content={"error":e}
        )

