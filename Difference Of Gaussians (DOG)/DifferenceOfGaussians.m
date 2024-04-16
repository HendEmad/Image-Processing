clc
clear all
close all
warning off
% Read image from the database of matlab (in gray scale)
e = imread('moon.tif');
%nexttile;
% Show the image
imshow(e)
% Applying two different gaussian 2D filters on the same image
gaussian1 = fspecial('Gaussian', 21, 10); % 21: image size, 10: image stadndard deviation
gaussian2 = fspecial('Gaussian', 21, 13);
% Getting DOG by subtraction the two gaussian signals(images)
dog = gaussian1 - gaussian2;
%{
conv2 is a mathematical operation which requires converting the image from unsigned integrate into double
- The converting is the first parameter, 
- The second parameter is the kernal which is the dog,
- The third parameter means that output should have the same structure as input.
%}
dogFilterImage = conv2(double(e), dog, 'same');
imshow(dogFilterImage);