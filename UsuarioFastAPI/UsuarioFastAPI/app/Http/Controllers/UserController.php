<?php

namespace App\Http\Controllers;

use App\Services\FastApiService;
use Illuminate\Http\Request;

class UserController extends Controller
{
    protected $fastApi;

    public function __construct(FastApiService $fastApi)
    {
        $this->fastApi = $fastApi;
    }

    public function inicio()
    {
        return view("formulario");
    }

    //Añadir usuario
    public function store(Request $request)
    {
        $usuarioNuevo = $request->validate([
            'txtNombre' => 'required',
            'txtEdad'=> 'required',
            'txtCorreo'=> 'required',
        ]);

        $usuarioNuevo = [
            'name' => $usuarioNuevo['txtNombre'],
            'age' => $usuarioNuevo['txtEdad'],
            'email' => $usuarioNuevo['txtCorreo'],
        ];

        try{

            $response = $this->fastApi->post('/addUsuarios/', $usuarioNuevo);

            return redirect()->route('usuario.inicio')
                ->with('success','Usuario guardado por FASTAPI');
        }catch(\Exception $e){
            return back()->with('error', 'No fue posible guardar');
        }
    }

    //MOstrar registros
    public function index()
    {
        try{
            $usuarios = $this->fastApi->get('/todosUsuarios/');
            return view('consulta', compact('usuarios'));

        } catch(\Exception $e){
            return back()->with('error', 'No se pudo obtener la lista de usuarios');
        }
    }

    //Eliminar
    public function destroy($id)
    {
        try {
            $response = $this->fastApi->delete("/eliminarUsuario/{$id}");
            return redirect()->route('usuario.index')
                ->with('success', 'Usuario eliminado por FASTAPI');
        } catch (\Exception $e) {
            return back()->with('error', 'No se pudo eliminar el usuario');
        }
    }

    //Actualizar
    public function edit($id)
    {
        try {
            $usuario = $this->fastApi->get("/usuario/{$id}");
            return view('editar', compact('usuario'));
        } catch (\Exception $e) {
            return back()->with('error', 'No se pudo obtener los datos del usuario');
        }
    }

    public function update(Request $request, $id)
    {
        $usuarioActualizado = $request->validate([
            'txtNombre' => 'required',
            'txtEdad'   => 'required',
            'txtCorreo' => 'required',
        ]);

        $usuarioActualizado = [
            'name'  => $usuarioActualizado['txtNombre'],
            'age'   => $usuarioActualizado['txtEdad'],
            'email' => $usuarioActualizado['txtCorreo'],
        ];

        try {
            $response = $this->fastApi->put("/actualizarUsuarios/{$id}", $usuarioActualizado);
            return redirect()->route('usuario.index')
                ->with('success', 'Usuario actualizado por FASTAPI');
        } catch (\Exception $e) {
            return back()->with('error', 'No se pudo actualizar el usuario');
        }
    }

}
