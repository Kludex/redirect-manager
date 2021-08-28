FROM python:3.9-slim

RUN useradd --create-home user
WORKDIR /home/user
USER user

ENV PATH=/home/user/.local/bin:$PATH

COPY ./requirements.txt /home/user/requirements.txt
COPY ./redirect_manager /home/user/redirect_manager

RUN pip install --user --upgrade pip==21.2.4 \
    && pip install --user -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "-m", "redirect_manager" ]
