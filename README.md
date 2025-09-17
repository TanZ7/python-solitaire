# เกมไพ่ Solitaire

เกมไพ่ Solitaire แบบคลาสสิก ที่สามารถเล่นได้ทั้งหมดบน Terminal

## คุณสมบัติ

-   **กฎคลาสสิก:** ใช้กฎของเกมแบบมาตรฐาน
-      
-   **การเคลื่อนย้ายไพ่ที่สมบูรณ์:**
    -   ย้ายไพ่ทีละใบ (จาก Waste ไป Tableau/Foundation, จาก Tableau ไป Foundation)
    -   ย้ายกลุ่มไพ่ระหว่างกอง Tableau
    -   
-   **กลไกหลักของเกม:**
    -   จั่วไพ่จากกอง Stock
    -   เปิดไพ่ที่คว่ำหน้าในกอง Tableau โดยอัตโนมัติ
    -   นำไพ่จากกอง Waste กลับมาเติมที่ Stock 
  
-   **ตรวจจับชัยชนะ:** เกมจะตรวจจับโดยอัตโนมัติเมื่อคุณชนะ และแสดงข้อความแสดงความยินดี

## สิ่งที่ต้องมี

-   Python 3.x

## วิธีการรันโปรแกรม

1.  **โคลนโปรเจค:**
    ```sh
    git clone https://github.com/TanZ7/python-solitaire.git
    cd python-solitaire
    ```

2.  **(ทางเลือก แนะนำให้ทำ) สร้างและเปิดใช้งาน virtual environment:**
    -   สำหรับ Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    -   สำหรับ macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **รันเกม:**
    ```sh
    python -m src.main
    ```

## วิธีการเล่น

ควบคุมเกมโดยการพิมพ์คำสั่งใน Terminal

### ชื่อเรียกกองไพ่

-   **กอง Tableau:** `t1`, `t2`, `t3`, `t4`, `t5`, `t6`, `t7`
-   **กอง Foundation:** `f1`, `f2`, `f3`, `f4`
-   **กอง Waste:** `w` หรือ `waste`

### คำสั่ง

-   **จั่วไพ่:**
    ```
    d
    ```
-   **ย้ายไพ่ใบเดียว:**
    -   รูปแบบ: `move [กองต้นทาง] [กองปลายทาง]`
    -   ตัวอย่าง: `move w t5` (ย้ายจาก Waste ไป Tableau 5)
    -   ตัวอย่าง: `move t1 f1` (ย้ายจาก Tableau 1 ไป Foundation 1)

-   **ย้ายไพ่เป็นกลุ่ม:**
    -   รูปแบบ: `move [กองต้นทาง] [จำนวนไพ่] [กองปลายทาง]`
    -   ตัวอย่าง: `move t2 3 t6` (ย้ายไพ่ 3 ใบบนสุดจาก Tableau 2 ไป Tableau 6)

-   **ออกจากเกม:**
    ```
    q
    ```
