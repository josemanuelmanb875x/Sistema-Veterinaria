# Script para iniciar el proyecto de Veterinaria
Write-Host "🏥 Iniciando Sistema de Veterinaria..." -ForegroundColor Cyan
Write-Host ""

# Iniciar Backend
Write-Host "📦 Iniciando Backend (FastAPI)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd c:\workspace\frontend\backend; Write-Host '🐍 Backend corriendo en http://127.0.0.1:8000' -ForegroundColor Green; python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000"

# Esperar 3 segundos
Start-Sleep -Seconds 3

# Iniciar Frontend
Write-Host "🎨 Iniciando Frontend (Astro)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd c:\workspace\frontend; Write-Host '⚡ Frontend corriendo en http://localhost:4321' -ForegroundColor Green; npm run dev"

# Esperar 5 segundos
Start-Sleep -Seconds 5

Write-Host ""
Write-Host "✅ Servidores iniciados correctamente" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Accede a:" -ForegroundColor Cyan
Write-Host "   Frontend: http://localhost:4321" -ForegroundColor White
Write-Host "   Backend:  http://127.0.0.1:8000/docs" -ForegroundColor White
Write-Host ""
Write-Host "🔑 Credenciales:" -ForegroundColor Cyan
Write-Host "   Email:    test@vet.com" -ForegroundColor White
Write-Host "   Password: test123" -ForegroundColor White
Write-Host ""
Write-Host "⚠️  Para detener: Cierra las ventanas de PowerShell que se abrieron" -ForegroundColor Yellow
Write-Host ""

# Abrir navegador automáticamente
Start-Sleep -Seconds 2
Start-Process "http://localhost:4321"
