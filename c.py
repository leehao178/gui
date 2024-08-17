import tkinter as tk
from tkinter import ttk

# 創建主窗口
root = tk.Tk()
root.title("工具")

# 自定義Treeview樣式以設定正常行高度
style = ttk.Style(root)
style.configure("Treeview", rowheight=20)  # 設定正常行高度

# 創建Treeview
tree = ttk.Treeview(root, columns=("Item", "File1", "File2"), show="headings")
tree.heading("Item", text="Item")
tree.heading("File1", text="File 1 Value")
tree.heading("File2", text="File 2 Value")

# 插入50筆示例數據，並在每個項目後插入一條背景為灰色的行來模仿網格線
for i in range(1, 51):
    item_name = f"RegistryKey{i}"
    value1 = f"Value{i}"
    value2 = f"Value{i}" if i % 10 != 0 else f"DifferentValue{i}"
    tree.insert("", "end", values=(item_name, value1, value2))

    # 插入一條背景為灰色的行來模仿網格線
    tree.insert("", "end", values=("", "", ""), tags=("gridline",))

    # 條件格式：如果兩個值不一樣，將背景設為紅色
    if value1 != value2:
        row_id = tree.get_children()[-2]  # -2 是因為後面還插入了一條背景為灰色的行
        tree.item(row_id, tags=("diff",))

# 定義標籤顏色
tree.tag_configure("diff", background="red")
tree.tag_configure("gridline", background="gray90")  # 將灰色行的背景設為淺灰色，模仿網格線

# 添加滾動條
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# 顯示Treeview
tree.pack(expand=True, fill="both")

# 運行主循環
root.mainloop()
