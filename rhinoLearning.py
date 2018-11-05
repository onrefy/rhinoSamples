import rhinoscriptsyntax as rs 
startSpeed = 2.5
endSpeed =  3
ptonSpeed = 3.1
start = []
end = []
pton = []
for i in range(100):
    start.append([i*startSpeed,0,0])
    end.append([i*endSpeed,10,0])
    pton.append([i*ptonSpeed+3,5,0])
    rs.AddArc3Pt(start[i],end[i],pton[i])
