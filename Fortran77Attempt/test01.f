      program test01      
      implicit none
      integer len, i, j, k, l, n, largenum, counter, lesslargenum
      parameter(len = 100)
      parameter(largenum = 1E+6)
      parameter(lesslargenum=1E+5)
      real a(len,2), c(len,2), q(lesslargenum,3)
      real x0,y0,xM,yM,xN,yN
      real px, py, cx, cy, m
      integer pointspercurve, qindex
      real t, dummyx,dummyy, dummy1, dummy2
      real px1, px2, px3, py1, py2, py3
      real px4, py4
C-----"'N' IS THE POINT OF MAX DIAMETER; 'M IS POINT OF MAX WIDTH'"---C
      parameter(xM=22)
      parameter(yM=27)
      parameter(xN=20)
      parameter(yN=27)
      parameter(pointspercurve=100)
      counter = 0
      open(10,file='bx.txt')
      open(11,file='by.txt')
      do 10 i = 1, largenum
        read(10,*,end=11)
        counter = counter + 1
10    continue
11    continue
      rewind(unit=10)
C-----"BEARING SEAT (DIMS IN MM)"-------------------------------------C
C-----"THESE COORDINATE PAIRS ARE IN ORDER"---------------------------C
      do 12 i = 1,counter
        read(10,*) a(i,1)
        read(11,*) a(i,2)
12    continue
C-----"THIS IS WHERE THE MAGIC HAPPENS: THE PROFILEE"-----------------C
C     "Start point (x0, y0)"
      x0 = a(counter,1)
      y0 = a(counter,2)
C     "open two more files, cx.txt and cy.txt that have all the"
C     "   coordinates of the points to be fit into the thing..."
      open(12,file='cx.txt')
      open(13,file='cy.txt')
      open(14,file='qout.out')
      counter = 0
C     "6.) Determine length of files as variable 'N' "
      do 15 i = 1, largenum
        read(12,*,end=13)
        counter = counter + 1
15    continue
13    continue
      rewind(unit=12)
      do 14 i=1,counter
        read(12,*) c(i,1)
        read(13,*) c(i,2)
14    continue
      n = counter
C     "Now that I have a list of points, I will loop through them"
C     "... and fit a quadratic bezier curve to it, unless it is the"
C     "... last point, in which case it will be cubic"
      if(n.ge.3) then
        m = 0
        counter = 0
        qindex=0
        do 16 i = 1,n
          if(i.eq.1) then
            counter = counter + 1
            cx = c(i,1)
            cy = c(i,2)
            px = 0.0
            py = 0.0
            call firstpoint(x0,y0,cx,cy,m,px,py)
            print*,((cy-py)/(cx-px))
            do 17 j = 1,pointspercurve
              t = (j/real(pointspercurve))
              qindex=qindex+1
              q(qindex,1)=qindex
              q(qindex,2)=(((1-t)**2)*x0)+((2*t*(1-t))*px)+((t**2)*cx)
              q(qindex,3)=(((1-t)**2)*y0)+((2*t*(1-t))*py)+((t**2)*cy)
              write(14,*)q(qindex,2), " ",q(qindex,3)
17          continue
          elseif(i.lt.n) then
            print*,m
            px1 = c(i-1,1)
            py1 = c(i-1,2)
            px2 = 0.0
            py2 = 0.0
            px3 = c(i,1)
            py3 = c(i,2)
            call everyotherpoint(px1,py1,px2,py2,px3,py3,m)
            do 18 j = 1, pointspercurve
              t = (j/real(pointspercurve))
              qindex = qindex + 1
              q(qindex,1)=qindex
              q(qindex,2)=((1-t)**2)*px1+2*t*(1-t)*px2+(t**2)*px3
              q(qindex,3)=((1-t)**2)*py1+2*t*(1-t)*py2+(t**2)*py3
              write(14,*)q(qindex,2)," ",q(qindex,3)
18          continue
          elseif(i.eq.n) then
          endif
16      continue
      else
        print*,"Not enough points in profile data file"
      endif
      end

      subroutine everyotherpoint(cx,cy,px2,py2,xN,yN,m)
        real cx,cy,px2,py2,xN,yN,m
        real num1, num2, den1, px1, py1
        px1 = cx
        py1 = cy
        px3 = xN
        py3 = yN
        print*,px1,py1,px3,py3
C        px2 = ((-((px1)**2))+(2*px1*m*(py3-py1))+(py1**2)-(2*py1*py3)+(
C     &  px3**2)+(py3**2))/(2*((px1)-(m*(py1-py3))-(px3)))
C        py2 = -(((m*(px1**2))-(2*px1*(py1+px3*m))-(m*(py1**2))+(2*py1*
C     &  px1)+(m*((px3**2)+(py3**2))))/(2*((px1)-(m*(py1-py3))-(px3))))
        m = (py3-py2)/(px3-px2)
      end subroutine

      subroutine firstpoint(x0,y0,cx,cy,m,px,py)
        real x0, y0, cx, cy, m
        real px1, px2, px3, py1, py2, py3
        px1 = x0
        py1 = y0
        px3 = cx
        py3 = cy
        px = px1
        py=(((px3-px1)**2)+(py3**2)-(py1**2))/(2*(py3-py1))
        m=(cy-py)/(cx-px)
      end subroutine
