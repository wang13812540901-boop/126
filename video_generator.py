#!/usr/bin/env python3
"""
AI视频生成示例
这个脚本使用OpenCV库生成一个简单的视频
"""

import cv2
import numpy as np
import os

def generate_basic_video():
    """生成一个基本的视频"""
    # 视频参数
    width, height = 640, 480
    fps = 24
    duration = 10  # 视频时长（秒）
    total_frames = fps * duration
    
    # 创建视频写入器
    output_path = 'output_video.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    print(f"正在生成视频，时长 {duration} 秒...")
    
    for i in range(total_frames):
        # 创建一个空白帧
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        
        # 添加一些动态元素
        # 计算当前进度
        progress = i / total_frames
        
        # 绘制一个移动的圆形
        x = int(width * progress)
        y = height // 2
        radius = 30
        color = (0, 255, 0)  # 绿色
        thickness = -1  # 填充
        
        cv2.circle(frame, (x, y), radius, color, thickness)
        
        # 添加文本
        text = f"AI 视频生成示例 - 帧 {i+1}/{total_frames}"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # 写入帧
        out.write(frame)
    
    # 释放资源
    out.release()
    print(f"视频生成完成！保存在: {output_path}")
    
    return output_path

def generate_pattern_video():
    """生成一个带有图案的视频"""
    # 视频参数
    width, height = 640, 480
    fps = 24
    duration = 5  # 视频时长（秒）
    total_frames = fps * duration
    
    # 创建视频写入器
    output_path = 'pattern_video.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    print(f"正在生成图案视频，时长 {duration} 秒...")
    
    for i in range(total_frames):
        # 创建一个空白帧
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        
        # 计算当前时间
        t = i / fps
        
        # 绘制动态图案
        for x in range(0, width, 20):
            for y in range(0, height, 20):
                # 计算颜色
                r = int(128 + 127 * np.sin(t + x/100))
                g = int(128 + 127 * np.sin(t + y/100))
                b = int(128 + 127 * np.sin(t + (x+y)/100))
                
                # 绘制方块
                cv2.rectangle(frame, (x, y), (x+15, y+15), (b, g, r), -1)
        
        # 添加文本
        text = f"图案视频示例"
        cv2.putText(frame, text, (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # 写入帧
        out.write(frame)
    
    # 释放资源
    out.release()
    print(f"图案视频生成完成！保存在: {output_path}")
    
    return output_path

if __name__ == "__main__":
    print("AI 视频生成工具")
    print("1. 生成基本移动圆形视频")
    print("2. 生成动态图案视频")
    
    choice = input("请选择要生成的视频类型 (1/2): ")
    
    if choice == '1':
        generate_basic_video()
    elif choice == '2':
        generate_pattern_video()
    else:
        print("无效选择，请重新运行脚本并选择 1 或 2")
