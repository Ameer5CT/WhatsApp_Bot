import sys
from wapp import wapp


group_name = "Bilgisayar Programcılığı - İngilizce"
# group_name = "A5CT Admin"
admin_name = "A5CT Admin"
driver = wapp.open_driver(group_name, admin_name)

if driver == 1:
    sys.exit("Error while opening driver.")


# Sends lecture time in all sections
def cmd_time(msg):
    use_text = ("Examples:-\n\n"
            "/Time SQL\n"
            "/Time C#\n"
            "/Time PYTHON\n"
            "/Time JAVA\n"
            "/Time C\n"
            "/Time SYSTEM\n"
            "/Time WEB\n\n"
            "/Time S1 (Section one schedule)")
    if msg == "":
        return use_text

    lectures = [
        [" CPP223 , DATABASE MANAGEMENT SYSTEMS , SQL ",
         "S1: Tuesday 14:00-17:00 D2305\n"
         "S2: Wednesday 14:00-17:00 D2303\n"
         "S3: Friday 14:00-17:00 D2305"],

        [" CPP225 , OBJECT ORIENTED PROGRAMMING - I , C# ",
         "S1: Friday 08:00-11:00 D2506\n"
         "S2: Friday 14:00-17:00 D2310\n"
         "S3: Friday 11:00-14:00 D2305"],

        [" CPP227 , DESIGNING IDENTITY AND RES. MAN. SYSTEMS ARCH. , PYTHON , PY ",
         "S1: Thursday 11:00-15:00 D2308\n"
         "S2: Tuesday 09:00-13:00 TB2-15\n"
         "S3: Wednesday 11:00-15:00 D2307"],

        [" CPP243 , VISUAL PROGRAMMING - I , JAVA ",
         "S1: Wednesday 14:00-17:00 D2309\n"
         "S2: Wednesday 11:00-14:00 D2315\n"
         "S3: Monday 11:00-14:00 D2310"],

        [" CPP253 , DATA STRUCTURES , C ",
         "S1: Thursday 08:00-11:00 D2304\n"
         "S2: Thursday 11:00-14:00 D2304\n"
         "S3: Wednesday 15:00-18:00 D2308"],

        [" CPP263 , SYSTEMS ANALYSIS AND DESIGN , SYSTEM ",
         "S1: Friday 11:00-14:00 D2312\n"
         "S2: Thursday 14:00-17:00 D2304\n"
         "S3: Thursday 14:00-17:00 D2304"],

        [" CPP273 , WEB SITE DESIGN AND CREATION - I , WEB , HTML , CSS , JAVASCRIPT , JS ",
         "S1: Friday 14:00-17:00 D2312\n"
         "S2: Friday 11:00-14:00 D2310\n"
         "S3: Friday 08:00-11:00 D2310"],

        [" SECTION 1 , S1 , 1 , SEC1 , SEC 1 , SEC-1 , SECTION1 , SECTION-1 ",
         "Tuesday: SQL 14:00-17:00 D2305\n"
         "Wednesday: Java 14:00-17:00 D2309\n"
         "Thursday: C 08:00-11:00 D2304\n"
         "                   Python 11:00-15:00 D2308\n"
         "Friday: C# 08:00-11:00 D2506\n"
         "              System 11:00-14:00 D2312\n"
         "              Web 14:00-17:00 D2312"],

        [" SECTION 2 , S2 , 2 , SEC2 , SEC 2 , SEC-2 , SECTION2 , SECTION-2 ",
         "Tuesday: Python 09:00-13:00 TB2-15\n"
         "Wednesday: Java 11:00-14:00 D2315\n"
         "                      SQL 14:00-17:00 D2303\n"
         "Thursday: C 11:00-14:00 D2304\n"
         "                   System 14:00-17:00 D2304\n"
         "Friday: Web 11:00-14:00 D2310\n"
         "              C# 14:00-17:00 D2310"],

        [" SECTION 3 , S3 , 3 , SEC3 , SEC 3 , SEC-3 , SECTION3 , SECTION-3 ",
         "Monday: Java 11:00-14:00 D2310\n"
         "Wednesday: Python 11:00-15:00 D2307\n"
         "                      C 15:00-18:00 D2308\n"
         "Thursday: System 14:00-17:00 D2304\n"
         "Friday: Web 08:00-11:00 D2310\n"
         "              C# 11:00-14:00 D2305\n"
         "              SQL 14:00-17:00 D2305"],
    ]

    for i in range(7):
        if (" " + msg.lower() + " ") in lectures[i][0].lower():
            text = ("Lecture time of: " + lectures[i][0].split(",")[0].strip() + "\n" +
                    lectures[i][0].split(",")[1].strip() + "\n\n" +
                    lectures[i][1])
            return text

    for i in range(7, 10):
        if (" " + msg.lower() + " ") in lectures[i][0].lower():
            text = ("Schedule of: " + lectures[i][0].split(",")[0].strip() + "\n\n" +
                    lectures[i][1])
            return text

    return "Couldn't recognize the lecture name or section.\n" + use_text


# Example command
def cmd_test(msg):
    # if user send "/Test Something" then the msg here equal "Something"
    # A code that uses msg
    # Return the result (The bot will send the return text as a message to the group)
    text = "Test: " + msg
    return text


# Runs when a new message arrive
def new_message_callback(msg):
    try:
        if msg[0] != "/":
            return

        if msg.lower().startswith("/time"):
            wapp.send_msg(driver, cmd_time(msg[5:].strip()))
            return

        if msg.lower().startswith("/test"):
            wapp.send_msg(driver, cmd_test(msg[5:].strip()))
            return

        wapp.send_msg(driver,
                      "Commands:-\n\n"
                      "/Time Lecture name\n"
                      "(Lecture time for all sections)\n\n"
                      "/Time S1\n"
                      "(Section schedule)")

    except Exception as e:
        print(f"Error new_message_callback(msg): {e}")


wapp.check_new_message(driver, new_message_callback)
driver.quit()
