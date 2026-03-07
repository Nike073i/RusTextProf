import browserSync from "browser-sync";

const bs = browserSync.create();

export function modifyStream() {
    return bs.stream();
}

export function configureDevServerTask({
    baseDir,
    port = 3000,
    index = "home.html"
}) {

    function serve() {
        bs.init({
            server: {
                baseDir,
                index,
            },
            port,
            notify: false,
        });
    }

    return serve;
}
