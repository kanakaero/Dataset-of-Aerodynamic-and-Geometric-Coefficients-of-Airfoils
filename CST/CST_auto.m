clc;clear;
%% import
import CST.*
import airfoilfit.*
import CST_airfoil_fit.*
%% Get a list of all txt files in the current folder, or subfolders of it.
fds = fileDatastore('OLD\*.dat', 'ReadFcn', @importdata);
file = fds.Files;
n = length(file);
%% Loop over all files reading them in and plotting them.
for i = 1 : n
    [error,DATA,Weights] = CST(file{i});
    [~ , name , ~ ] = fileparts(file{i});
    filename = fullfile('D:\ENGINEERING\Misc\PROJECTS\Manikandan Sir - AI and ML for aerofoil selection\TEST\FINAL VERSION\Code 2 v4 FINAL AIRFOILTOOLS\OLD\PLOT',[name,'.png']);
    % Save the file as PNG
    exportgraphics(gcf,filename);
    % Save data in .dat format
    save(file{i}, 'DATA', '-ascii');
    % writetable(W, file)
    % Modify File Path
    [filepath, name, ~] = fileparts(file{i});
    file{i} = fullfile(filepath,[name, '_Coeffs.txt']);
    % Save Coeffs
    save(file{i}, 'Weights', '-ascii');
    close(gcf)
end