!    -*- f90 -*-
! -*- coding: utf-8 -*-
! written by Ralf Biehl at the Forschungszentrum Juelich ,
! Juelich Center for Neutron Science 1 and Institute of Complex Systems 1
!    jscatter is a program to read, analyse and plot data
!    Copyright (C) 2020-2021  Ralf Biehl
!
!    This program is free software: you can redistribute it and/or modify
!    it under the terms of the GNU General Public License as published by
!    the Free Software Foundation, either version 3 of the License, or
!    (at your option) any later version.
!
!    This program is distributed in the hope that it will be useful,
!    but WITHOUT ANY WARRANTY; without even the implied warranty of
!    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
!    GNU General Public License for more details.
!
!    You should have received a copy of the GNU General Public License
!    along with this program.  If not, see <http://www.gnu.org/licenses/>.
!

module dynamic
    use typesandconstants
    use utils
    !$ use omp_lib
    implicit none

contains

    function bnmt(t, NN, l, mu, modeamplist, tp)
        ! Rouse/Zimm mode summation coherent +incoherent +modeamplitudes

        ! times, mu, modeamplitudes, relaxation times, bond length
        real(dp), intent(in) :: t(:), mu, modeamplist(:), tp(:), l
        ! number beads, mode numbers n,m
        integer, intent(in)  :: NN
        ! result (n*m,tcoh + tinc + mode amplitudes (as t_inf))
        real(dp)             :: bnmt(NN*NN, 2*size(t) + size(modeamplist))
        ! internal stuff
        integer              :: p, n, m

        ! init
        bnmt = 0_dp
        !$omp parallel do
        do m = 1, NN
            do n = 1, NN
                do p = 1, size(modeamplist)
                    bnmt((n-1)*NN+m,:size(t)) = bnmt((n-1)*NN+m,:size(t)) + &
                            modeamplist(p) * cos(pi_dp * p * n / NN) * cos(pi_dp * p * m / NN) * (1 - exp(-t/tp(p)))
                    ! each p for mode amplitudes and later infinite time is sum_p( mode amplitudes)
                    bnmt((n-1)*NN+m,2*size(t)+p) = bnmt((n-1)*NN+m,2*size(t)+p) + &
                            modeamplist(p) * cos(pi_dp * p * n / NN) * cos(pi_dp * p * m / NN)
                    if (n == m) then
                        bnmt((n-1)*NN+m,size(t):2*size(t)) = bnmt((n-1)*NN+m,size(t):2*size(t)) + &
                                modeamplist(p) * cos(pi_dp * p * n / NN) **2  * (1 - exp(-t/tp(p)))
                    end if
                end do
                bnmt((n-1)*NN+m,:) = bnmt((n-1)*NN+m,:) + (abs(n - m) ** (2 * mu) * l ** 2)
            end do
        end do
        !$omp end parallel do

    end function bnmt




end module dynamic