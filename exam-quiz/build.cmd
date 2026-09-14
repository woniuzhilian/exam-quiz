@echo off
setlocal enabledelayedexpansion
REM 使用 QClaw 自带 Node 运行时执行构建（本机未单独安装 Node.js）
REM 用法：双击本文件，或在项目目录里执行  build.cmd

set "NODE_EXE="
for /f "delims=" %%I in ('dir /b /s "C:\Program Files\QClaw\v*\resources\node\node.exe" 2^>nul') do set "NODE_EXE=%%I"

set "NPM_JS="
for /f "delims=" %%I in ('dir /b /s "C:\Program Files\QClaw\v*\resources\openclaw\config\npm-tools\node_modules\npm\bin\npm-cli.js" 2^>nul') do set "NPM_JS=%%I"

if "%NODE_EXE%"=="" (
  echo [错误] 未找到 QClaw 自带 Node 运行时，请确认 QClaw 安装目录存在。
  pause
  exit /b 1
)
if "%NPM_JS%"=="" (
  echo [错误] 未找到 npm-cli.js。
  pause
  exit /b 1
)

for %%A in ("%NODE_EXE%") do set "NODE_DIR=%%~dpA"
set "PATH=%NODE_DIR%;%PATH%"

cd /d "%~dp0"
echo === 正在构建 (vite build) ===
"%NODE_EXE%" "%NPM_JS%" run build
echo.
echo === 构建结束，dist 目录已更新 ===
echo 下一步：把 dist 目录拖到 https://app.netlify.com/drop
pause
