def solution(video_len, pos, op_start, op_end, commands):
    posTime = pos.split(':')
    videoTime = video_len.split(':')
    opStart = op_start.split(':')
    opEnd = op_end.split(':')

    posMill = int(posTime[0]) * 60 + int(posTime[1])
    videoLenMill = int(videoTime[0]) * 60 + int(videoTime[1])
    opStartMill = int(opStart[0]) * 60 + int(opStart[1])
    opEndMill = int(opEnd[0]) * 60 + int(opEnd[1])


    currentPos = posMill

    for command in commands:
        if currentPos >= opStartMill and currentPos <= opEndMill:
            currentPos = opEndMill
    
        if command == 'prev':
            if currentPos < 10:
                currentPos = 0
            else:
                currentPos -= 10
        else:
            if videoLenMill - currentPos < 10:
                currentPos = videoLenMill
            else:
                currentPos += 10

    if currentPos >= opStartMill and currentPos <= opEndMill:
        currentPos = opEndMill

    min = currentPos // 60
    sec = currentPos % 60

    minStr = str(min)
    secStr = str(sec)
        
    if min < 10:
        minStr = f"0{minStr}"
    
    if sec < 10:
        secStr = f"0{secStr}"

    return f"{minStr}:{secStr}"