import { src, dest, parallel } from "gulp";

export function configureCopyMediaTask({
    mediaOptions
}) {

    function createCopyTask({
        fromSrc,
        toDist
    }) {
        return () => src([
            `${fromSrc}/**/*`
        ], { encoding: false }).pipe(dest(`${toDist}/`))
    }

    const copyTasks = mediaOptions.map(createCopyTask);

    return parallel(copyTasks);
}