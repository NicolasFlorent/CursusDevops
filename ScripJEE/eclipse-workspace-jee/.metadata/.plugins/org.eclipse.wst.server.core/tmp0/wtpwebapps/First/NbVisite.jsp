<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.util.*" %>
<%-- <%@ taglib uri = "http://java.sun.com/jsp/jstl/core" prefix = "c" %>--%>
 <!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Page selon le nombre de visite !</title>
</head>
<body>

<%-- Déclaration de la variable globale --%>
<%!int nbVisite=0; %>

<%--Définition du code Java --%>

<%
Date date = new Date();
nbVisite++;
String aff="";
if (nbVisite%2==0)
	aff="<img src= https://parismatch.be/app/uploads/2018/04/Macaca_nigra_self-portrait_large-e1524567086123-1100x715.jpg>";
	else
		aff="<p>lorem</p>";
%>

<h1>TP2</h1>
<hr>
<%=aff %>

</body>
</html>