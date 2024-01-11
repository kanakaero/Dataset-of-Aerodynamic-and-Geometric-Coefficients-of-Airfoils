function [ME,DATA,Weights] = CST(file)
% Load the airfoil data
fid = fopen(file);
firstLine = fgetl(fid); % read the first line of the file
if ischar(firstLine) % check if the first line is a character string
    fgetl(fid);
    A = readmatrix(file); % read in the data skipping the first row
else
    A = readmatrix(file); % read in the data without skipping any row 
end
fclose(fid);
x = A(:,1);                   % X coordinates from the imported data
y = A(:,2);                   % Y coordinates from the imported data

%% Upper and Lower Surfaces

% Find the y-coordinate where x is closest to zero
[~,ind] = min(abs(x));

% Separate the X_upper and X_lower coordinates
XL = x(1:ind-1);
XU = x(ind:end);

%% CST CODE
xcoord = x;
yt     = y;
dz     = 0;

%% CST Method

Winit = [-1 -1 -1 -1 1 1 1 1];      % initial weights

% Run the optimization code

[Wopt]=fmincon(@(W) airfoilfit(W,yt,XL,XU,0),Winit,[],[],[],[],ones(1,8)*-1,ones(1,8),[]);

%% Airfoil Using CST Method
x_lower = linspace(0,1,300)';
x_upper = linspace(0,1,300);
x_Upper = sort(x_upper,'descend')';
w = Wopt;
W = [w(1) w(2) w(3) w(4) w(5) w(6) w(7) w(8)];
[ycoord,yl,yu] = CST_airfoil_fit(Wopt,x_lower,x_Upper,dz); % Airfoil generated from CST weights
Xcoord = [x_lower;x_Upper];
%% ERROR
x = x';
Xcoord = Xcoord';
error =[];
for i = 1:length(A)
    k = find(x(i) == Xcoord);
    difference= ycoord(k) - yt(i);
    e = difference/yt(i);
    error = [error,e];
    i = i+1;
end
ME = sum(error,'all')/length(error);
% MeanSquaredError = difference.^2;
% MeanSquaredError = sum(MeanSquaredError)/length(A);
%% Plot and compare
plot(xcoord,yt,'LineWidth',2,'Color',[0 1 1])
hold on
plot(Xcoord,ycoord,'k--','LineWidth',1)
axis equal
set(gcf,'color','w')

set(gca, ...
  'Box'         , 'on'     , ...
  'TickDir'     , 'in'     , ...
  'TickLength'  , [.015 .015] , ...
  'XMinorTick'  , 'off'      , ...
  'YMinorTick'  , 'off'      , ...
  'YGrid'       , 'on'      , ...
  'XGrid'       , 'on'      , ...
  'XColor'      , [.01 .01 .01], ...
  'YColor'      , [.01 .01 .01], ...
  'xlim'        , ([0 1]),...
  'ylim'        , ([-0.2 0.2]),...
  'YTick'       , -0.2:0.1:0.2, ...
  'XTick'       , 0:0.1:1,...
  'LineWidth'   , 1);

ax = gca;
ax.GridColor = [0 0 0];
ax.GridLineStyle = ':';
% ax.GridLineWidth = 0.2;
ax.GridAlpha = 0.1;
ax.Layer = 'top';

xlabel('Xcoord',...
       'FontUnits'  ,'points',...
       'Interpreter','latex',...
       'FontSize'   , 11,...
       'FontName'   , 'AvantGarde');

ylabel('Ycoord',...
       'FontUnits'  ,'points',...
       'Interpreter','latex',...
       'FontSize'   , 11,...
       'FontName'   , 'AvantGarde');

leg3 = legend('Target','CST');
%% WRITING
x_Upper = sort(x_Upper,'ascend');
x_lower = sort(x_lower,'descend');
Xcoord = [x_Upper;x_lower];
Ycoord = [yl;yu];
DATA = [Xcoord,Ycoord];
Weights = [Wopt(1) Wopt(2) Wopt(3) Wopt(4) Wopt(5) Wopt(6) Wopt(7) Wopt(8)];
end