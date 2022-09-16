# 3ds-upload

Webserver to upload images from your 3DS/Wii U console.

## Ideas

- Delete after X time
- Modal when clicked
  - Upload date
  - Console Uploaded from
- Only allow images with 3ds screen size

## Console Limitations

### Wii U

On the Wii U, you can upload screenshots from your games.

### 3DS

On the 3DS (Old and New), you can upload screenshots from your games, and images from your SD card.

## Gallery

![image](https://user-images.githubusercontent.com/66192059/190689072-e58537bb-c6f8-49db-9aa1-4a7b2efa5d01.png)
![image](https://user-images.githubusercontent.com/66192059/190689105-a9f11a4c-09fe-4cc8-98f5-4e81becb6870.png)
![image](https://user-images.githubusercontent.com/66192059/190690381-0cd4898a-246c-4c19-ad5c-2428de196f13.png)
![image](https://user-images.githubusercontent.com/66192059/190696828-4ecc0593-83b7-4250-b804-136216c6b9a8.png)

## Setup

In order to use this, you will need Flask and Colorama.

Set `config.py` to your liking and run `py app.py`!

### Windows Copy-Paste

    py -m venv venv
    cd venv
    cd scripts
    activate
    cd ..
    cd ..
    py -m pip install flask colorama
    py app.py

## Configuration

| Name           | Default Value  | Type    | Description |
| :------------- | :------------- | :------ | :---------- |
| `loc`          | `./uploads/`   | String  | Location of uploaded images        |
| `locname`      | `uploads`      | String  | Name of image location             |
|                |                |         |                                    |
| `debug`        | `True`         | Boolean | Enables Flask Debug                |
| `url`          | `192.168.0.34` | String  | URL the server is hosted           |
| `port`         | `80`           | Integer | Port to host the server on         |
| `secret_key`   | `ChangeMe586`  | String  | **CHANGE THIS!** Secret Key        |
| `local`        | `True`         | Boolean | Flag if the server is local        |
|                |                |         |                                    |
| `imglimit`     | `None`         | Integer | Limit of images to show on /list   |
| `consolelimit` | `3`            | Integer | Limit of images to show on console |
