      program xmatmul
        implicit none

        integer i,j
        integer, parameter :: M=2,N=3

        real :: a(M,N) = reshape((/1.0,4.0,2.0,5.0,3.0,6.0/),(/M,N/))
        real :: b(N,M) = reshape((/1.0,2.0,3.0,4.0,5.0,6.0/),(/N,M/))
        real :: c(M,M)
        integer :: clock0, clock1, clockmax, clockrate, ticks
        real    :: secs

        call system_clock(count_max=clockmax, count_rate=clockrate)
        call system_clock(clock0)

        write(*,*) 'Matrix [a]'
        do i=1,M
          write(*,1000) (a(i,j),j=1,N)
        enddo
        write(*,*)

        write(*,*) 'Matrix [b]'
        do i=1,N
          write(*,1000) (b(i,j),j=1,M)
        enddo
        write(*,*)

        c = matmul(a, b)
        write(*,*) 'Matrix [c] = [a] x [b]'
        do i = 1,M
          write(*,1000) (c(i,j),j=1,M)
        enddo
        write(*,*)
        call system_clock(clock1)
        ticks = clock1-clock0
        ticks = mod(ticks+clockmax, clockmax)
        secs = float(ticks)/float(clockrate)
        write(*,*) 'Code took ', secs, ' seconds'
1000  FORMAT(1x,1P10E14.6)
      end program xmatmul

!#################################################################################
!Sources:
!http://www.nr.com/forum/showthread.php?t=1434
!http://www.hpcx.ac.uk/support/documentation/UserGuide/HPCxuser/Porting_Codes.html
!#################################################################################
