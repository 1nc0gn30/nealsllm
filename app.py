# app.py
import pygame
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Pygame setup
WIDTH, HEIGHT = 400, 300
ball_pos = [200, 150]
ball_vel = [2, 2]
BALL_RADIUS = 15

def update_ball():
    global ball_pos, ball_vel

    # Update the ball's position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Check for collision with walls and reverse velocity
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

@app.route('/get_ball', methods=['GET'])
def get_ball():
    update_ball()
    return jsonify({
        "ball_pos": ball_pos
    })

@app.route('/change_velocity', methods=['POST'])
def change_velocity():
    global ball_vel
    data = request.json
    if "vx" in data and "vy" in data:
        ball_vel = [data["vx"], data["vy"]]
    return jsonify({"status": "success", "ball_vel": ball_vel})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
