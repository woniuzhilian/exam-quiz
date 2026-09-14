@echo off
setlocal enabledelayedexpansion
REM 使用 QClaw 自带 Node 运行时启动本地测试服务器
REM 用法：双击本文件，然后浏览器打开 http://localhost:5173/

set "NODE_EXE="
for /f "delims=" %%I in ('dir /b /s "C:\Program Files\QClaw\v*\resources\node\node.exe" 2^>nul') do set "NODE_EXE=%%I"

set "NPM_JS="
for /f "delims=" %%I in ('dir /b /s "C:\Program Files\QClaw\v*\resources\openclaw\config\npm-tools\node_modules\npm\bin\npm-cli.js" 2^>nul') do set "NPM_JS=%%I"

if "%NODE_EXE%"=="" (
  echo [错误] 未找到 QClaw 自带 Node 运行时。
  pause
  exit /b 1
)

for %%A in ("%NODE_EXE%") do set "NODE_DIR=%%~dpA"
set "PATH=%NODE_DIR%;%PATH%"

cd /d "%~dp0"
echo === 启动本地测试服务器 (npm run dev) ===
echo 浏览器打开：http://localhost:5173/
"%NODE_EXE%" "%NPM_JS%" run dev
pause
