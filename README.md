# Invoice AI Extractor

This project extracts structured data from invoice images using OCR and AI.

## Features

* Upload invoice image
* Extract text using Tesseract OCR
* Parse structured invoice data using Google Gemini AI
* Store results in Supabase database
* REST API built with FastAPI
* Deployed on Render

## Tech Stack

* FastAPI
* Python
* Google Gemini API
* Tesseract OCR
* Supabase
* Render

## API Endpoints

### GET /

Health check endpoint

### POST /upload

Upload invoice image

### POST /process

Extract OCR text and parse structured invoice data

## Deployment

API URL:
https://invoice-ai-extractor.onrender.com

Swagger Docs:
https://invoice-ai-extractor.onrender.com/docs

## Setup

Install dependencies:

pip install -r requirements.txt

Run locally:

uvicorn backend.main:app --reload

## Environment Variables

GEMINI_API_KEY=your_gemini_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
