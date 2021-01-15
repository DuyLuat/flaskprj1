$(document).ready(function () {
    $(".delele-btn").click(function (event) {
        if (!confirm('Dữ liệu bị xoá sẽ không thể khôi phục. Bạn vẫn muốn tiếp tục')) {
            event.preventDefault();
            return false;
        }

        return true;
    });

    $(".btn-del-art").click(function (event) {
        if (!confirm('Bài viết sẽ bị xóa. Bạn có muốn tiếp tục không?')) {
            event.preventDefault();
            return false;
        }

        return true;

    });
    $(".btn-restore-art").click(function (event) {
        if (!confirm('Bạn có chắc chắn muốn khôi phục không?')) {
            event.preventDefault();
            return false;
        }

        return true;
    });

    $(".btn-destroy").click(function (event) {
        if (!confirm('Bạn sẽ không thể khôi phục dữ liệu này nữa. Có chắn chắn sẽ tiếp tục')) {
            event.preventDefault();
            return false;
        }
        return true;
    });
    
    $("div.alert").delay(3000).slideUp();

});