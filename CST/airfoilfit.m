function error = airfoilfit(W,yt,xl,xu,dz)
% Input :
% W = CST weights
% yt = y-coordinate of the target airfoil
% xl = x-coordinate of the lower surface
% xu = y-coordinate of the upper surface
% dz = trailing edge thickness, match this with the target airfoil

% note: Here I assume that the upper and lower surface have the same amount
% of weights. The arrangement for W is :
% [wl wu], where wl and wu are the lower and upper surface CST weights,
% repsectively. So for example if the wl is [-1 -1 -1] and wu is [1 1 1],
% then W becomes [-1 -1 -1 1 1 1]

yp = CST_airfoil_fit(W,xl,xu,dz); % Airfoil generated from CST weights

error = mean(abs(yt-yp)); % Minimize this error