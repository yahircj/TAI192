<?php

use App\Http\Controllers\UserController;
use Illuminate\Support\Facades\Route;

Route::get('/', [UserController::class, 'inicio'])->name('usuario.inicio');
Route::post('/addUser', [UserController::class, 'store'])->name('usuario.store');
Route::get('/usuarios', [UserController::class, 'index'])->name('usuario.index');

// Rutas para edición y actualización
Route::get('/usuario/edit/{id}', [UserController::class, 'edit'])->name('usuario.edit');
Route::put('/usuario/update/{id}', [UserController::class, 'update'])->name('usuario.update');

// Ruta para eliminación
Route::delete('/usuario/delete/{id}', [UserController::class, 'destroy'])->name('usuario.destroy');
