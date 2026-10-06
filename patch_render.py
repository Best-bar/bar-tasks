import re

with open('index.html', 'r') as f:
    content = f.read()

search = """      } else if (!task.inWork) {
        resultHtml = `
          <div class="result-container" id="inWorkBox_${safeId}">
            <button type="button" class="btn-in-work" id="btnInWork_${safeId}" onclick="takeTaskInWorkAction('${task.barName}', ${task.rowIdx}, '${safeId}')">
              🛠️ Взять в работу
            </button>
          </div>`;
      } else {
        resultHtml = `
          <div class="result-container" id="resBox_${safeId}">
            <div class="result-form-block">
              <div class="result-input-row">
                <input type="text" id="resInput_${safeId}" placeholder="Опишите результат выполнения...">
                <button type="button" class="btn-res-submit" onclick="submitTaskResult('${task.barName}', ${task.rowIdx}, '${safeId}')">Выполнено</button>
              </div>
              <label class="btn-res-photo" for="resFile_${safeId}" id="resFileLbl_${safeId}">📎 Прикрепить фото отчета (до 10)</label>
              <input type="file" id="resFile_${safeId}" accept="image/*,.heic,.heif" multiple style="display:none;" onchange="handleResultFileSelect(this, ${task.rowIdx}, '${safeId}')">
              <div style="display:flex; align-items:center; gap:8px; margin-top:2px;">
                <img id="resThumb_${safeId}" class="thumb-preview" src="">
                <span id="resFileName_${safeId}" style="font-size:11px; color:var(--text-secondary);"></span>
              </div>
            </div>
          </div>`;
      }"""

replace = """      } else if (currentUserRole !== 'admin' && currentUserRole !== 'executor') {
        if (!task.inWork) {
          resultHtml = `
            <div class="result-container" style="text-align:center; padding:10px; color:var(--text-secondary); font-size:12px;">
              Ожидает исполнителя
            </div>`;
        } else {
          resultHtml = `
            <div class="result-container" style="text-align:center; padding:10px; color:var(--warning-color); font-size:12px;">
              🟡 В работе
            </div>`;
        }
      } else if (!task.inWork) {
        resultHtml = `
          <div class="result-container" id="inWorkBox_${safeId}">
            <button type="button" class="btn-in-work" id="btnInWork_${safeId}" onclick="takeTaskInWorkAction('${task.barName}', ${task.rowIdx}, '${safeId}')">
              🛠️ Взять в работу
            </button>
          </div>`;
      } else {
        resultHtml = `
          <div class="result-container" id="resBox_${safeId}">
            <div class="result-form-block">
              <div class="result-input-row">
                <input type="text" id="resInput_${safeId}" placeholder="Опишите результат выполнения...">
                <button type="button" class="btn-res-submit" onclick="submitTaskResult('${task.barName}', ${task.rowIdx}, '${safeId}')">Выполнено</button>
              </div>
              <label class="btn-res-photo" for="resFile_${safeId}" id="resFileLbl_${safeId}">📎 Прикрепить фото отчета (до 10)</label>
              <input type="file" id="resFile_${safeId}" accept="image/*,.heic,.heif" multiple style="display:none;" onchange="handleResultFileSelect(this, ${task.rowIdx}, '${safeId}')">
              <div style="display:flex; align-items:center; gap:8px; margin-top:2px;">
                <img id="resThumb_${safeId}" class="thumb-preview" src="">
                <span id="resFileName_${safeId}" style="font-size:11px; color:var(--text-secondary);"></span>
              </div>
            </div>
          </div>`;
      }"""

if search in content:
    content = content.replace(search, replace)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Search block not found")
