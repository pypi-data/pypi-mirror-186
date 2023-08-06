import os

def router( name ):
    file_router = open(f"app/routers/{ name }.py", "w")
    file_router.write("from fastapi import APIRouter, Request \n")
    file_router.write("from app.utils.view import Template" + os.linesep)
    file_router.write(os.linesep)
    file_router.write(f"router = APIRouter( prefix = '/{ name.replace( '_', '-' ) }', tags = ['{ name.replace( '_', '-' ) }'] )" + os.linesep)
    file_router.write(f"class { name }:" + os.linesep)

    file_router.write(f"    @router.get('/') \n")
    file_router.write(f"    async def index( request: Request ): \n")
    file_router.write(f"        return Template.view( 'name_view', request )" + os.linesep)

    file_router.close()

    include_route( name )
    import_route( name )

    print( f'Archivo generado en: /app/routers/{ name }.py' )

def include_route( name ):
    file_main = open('main.py', "a")
    file_main.write(f"\napp.include_router( {name}.router )")
    file_main.close()

def import_route( name ):
    file_imports_main = open('imports_main.py', "a")
    file_imports_main.write(f"\nfrom app.routers import {name}")
    file_imports_main.close()