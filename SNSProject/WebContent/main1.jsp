<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>

<html lang="ko">

<!--해드 -->
<%@ include file= "htmltegs/head.jsp" %>

<body>

    <!--해더 -->
    <%@ include file= "htmltegs/header.jsp" %>
    
    <!-- 네비 : 하이퍼링크 -->
    <%@ include file= "htmltegs/nav.jsp" %>


        <!-- Section : 내부에 article 있음-->
        <section id="section" class="phone" >   

            <article id="article" >

                <div class="MyPageBox">
                    <table class="Profile">

                        <tr>
                            <th rowspan="3">
                               <div class="Profile_Photo"><img src="https://placeimg.com/130/130/any" ></div>
                            </th>
                            <td>이름</td>
                            <td>포인트</td>
                            <td>충전</td>
                        </tr>
                        <tr>
                            <td>팔로우</td>
                            <td>좋아요</td>
                            <td>게시글</td>
                        </tr>
                        <tr>
                            <td>30</td>
                            <td>50</td>
                            <td>10</td>
                        </tr>
                    </table>
                </div>
                <div class="MyPageBox"> <h3>공지사항</h3> </div>
                <div class="MyPageBox"> <h3>실시간 문의</h3> </div>
                <div class="MyPageBox"> <h3>친구에게 공유</h3> </div>
                <div class="MyPageBox"> <a href="main0.jsp"> <h3>로그아웃</h3> </a> </div>
                

            </article>

        </section>
    <!-- 푸터 -->
    <%@ include file= "htmltegs/footer.jsp" %>
    
</body>
</html>