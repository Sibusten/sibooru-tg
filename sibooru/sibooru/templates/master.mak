<!DOCTYPE html>
<html>
<head>
  <%block name="head">
    <title><%block name="title">Sibooru</%block></title>

    <link rel="stylesheet" type="text/css" href="${tg.url('/css/bootstrap.min.css')}"/>
    <link rel="stylesheet" type="text/css" href="${tg.url('/css/base.css')}"/>
  </%block>
</head>
<body>
  <div class="header">
    The header
  </div>
  <%block name="content" />
  <div class="footer">
    The footer
  </div>
</body>
</html>
