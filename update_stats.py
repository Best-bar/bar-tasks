import re

with open('index.html', 'r') as f:
    content = f.read()

search_block = """    function renderStatistics() {
      const barSel = document.getElementById('statsBarSelect').value;
      const initSel = document.getElementById('statsInitiatorSelect').value;

      const filtered = allTasksCached.filter(task => {
        const mBar = (barSel === "ALL") || (task.barName === barSel);
        const mInit = (initSel === "ALL") || (task.initiator && task.initiator.toLowerCase().trim() === initSel);
        return mBar && mInit;
      });"""

replace_block = """    function renderStatistics() {
      const barSel = document.getElementById('statsBarSelect').value;
      const initSel = document.getElementById('statsInitiatorSelect').value;
      const typeSel = document.getElementById('statsTypeSelect') ? document.getElementById('statsTypeSelect').value : "ALL";
      const monthSel = document.getElementById('statsMonthSelect') ? document.getElementById('statsMonthSelect').value : "ALL";

      const filtered = allTasksCached.filter(task => {
        const mBar = (barSel === "ALL") || (task.barName === barSel);
        const mInit = (initSel === "ALL") || (task.initiator && task.initiator.toLowerCase().trim() === initSel);
        const mType = (typeSel === "ALL") || (task.type && task.type.toLowerCase().trim() === typeSel);

        let mMonth = true;
        if (monthSel !== "ALL") {
          const tDate = parseTaskDate(task.date);
          if (tDate) {
            mMonth = (tDate.getMonth() === parseInt(monthSel, 10));
          } else {
            mMonth = false;
          }
        }
        return mBar && mInit && mType && mMonth;
      });"""

if search_block in content:
    content = content.replace(search_block, replace_block)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Success")
else:
    print("Search block not found")
