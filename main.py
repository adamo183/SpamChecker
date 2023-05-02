from fastapi import FastAPI, Response, status
import machine_learning.spam_checker


app = FastAPI()


@app.post("/email/spam/check", status_code=200)
async def check_is_email_spam(data_to_check: str, response: Response):
    print(data_to_check)
    response.status_code = status.HTTP_200_OK
    return "Data: " + str(data_to_check)
