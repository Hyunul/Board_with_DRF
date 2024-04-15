const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
    app.use(
        createProxyMiddleware('/post', { // 사용할 엔드포인트
            target: 'http://localhost:8000', // 요청할 서버 주소
            changeOrigin: true, // 호스트가 헤더 변경 가능 옵션
        })
    );
    app.use(
        createProxyMiddleware('/user', { // 사용할 엔드포인트
            target: 'http://localhost:8000', // 요청할 서버 주소
            changeOrigin: true, // 호스트가 헤더 변경 가능 옵션
        })
    )
};