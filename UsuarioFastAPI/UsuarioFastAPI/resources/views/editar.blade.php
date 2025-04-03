<!-- resources/views/editar.blade.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Usuario</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
         <h1 class="display-3 text-center text-primary">Editar Usuario</h1>
         @if(session('error'))
            <div class="alert alert-danger">{{ session('error') }}</div>
         @endif
         <form action="{{ route('usuario.update', $usuario['id']) }}" method="POST">
              @csrf
              @method('PUT')
              <div class="mb-3">
                 <label class="form-label">Nombre:</label>
                 <input type="text" name="txtNombre" class="form-control" value="{{ $usuario['name'] }}" required>
              </div>
              <div class="mb-3">
                 <label class="form-label">Edad:</label>
                 <input type="number" name="txtEdad" class="form-control" value="{{ $usuario['age'] }}" required>
              </div>
              <div class="mb-3">
                 <label class="form-label">Correo:</label>
                 <input type="email" name="txtCorreo" class="form-control" value="{{ $usuario['email'] }}" required>
              </div>
              <button type="submit" class="btn btn-primary">Actualizar</button>
         </form>
         <a href="{{ route('usuario.index') }}" class="btn btn-dark mt-3">Cancelar</a>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
