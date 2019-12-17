<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>

<html lang="ko">

<!--해드 -->
<%@ include file= "htmltegs/head.jsp" %>

<body>
    <!--해더 -->
    <%@ include file= "htmltegs/header.jsp" %>
     
    <!-- 네비 : 하이퍼링크 -->
    <nav  id="nav" class="phone">   
            <table>
                <tr>
                    <td class="menu">  <a href="main1.jsp"> 마이페이지</a> </td>    
                    <td class="menu">  <a href="main2.jsp"> 포인트 벌기</a> </td>    
                    <td class="menu">  <a href="main3.jsp"> 의뢰 </a> </td>    
                    <td class="menu_active">  <a href="main4.jsp"> 의뢰현황 </a> </td>     
                </tr>
            </table>
        </nav >
        <!-- Section : 내부에 article 있음-->
        <section id="section" class="phone" >   
<article>
    <%@ include file= "htmltegs/Qtable.jsp" %>
    <%@ include file= "htmltegs/Qtable.jsp" %>
    <%@ include file= "htmltegs/Qtable.jsp" %>
    <%@ include file= "htmltegs/Qtable.jsp" %>
    <%@ include file= "htmltegs/Qtable.jsp" %>
    <%@ include file= "htmltegs/Qtable.jsp" %>
    <%@ include file= "htmltegs/Qtable.jsp" %>
    <%@ include file= "htmltegs/Qtable.jsp" %>
    <%@ include file= "htmltegs/Qtable.jsp" %>

                    

            </article>

        </section>
        
    <!-- 푸터 -->
    <%@ include file= "htmltegs/footer.jsp" %>

    <script>resize("leftBox");</script>
</body>
</html>