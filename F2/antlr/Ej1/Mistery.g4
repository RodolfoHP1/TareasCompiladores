grammar Mistery;

prog:	(Aa)* ;


Aa:	ID ('[' (ID | INTEGER) ']') +
//Aa:	ID ('[' Aa ']') +
    ;


ID: Letter LetterOrDigit*;
INTEGER : [0-9]+ ;

// fragment es para crear segmentos de token que solamente serán usados en este archivo, pero que no
// generan un token. Son como definiciones "locales" a este archivo.

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;

fragment Letter : [a-zA-Z$_] ;