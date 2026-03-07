import { src, dest } from "gulp";

export function configureCopyExamplesTask({
    fromSrc,
    toDist
}) {
    function copyExamples() {
        return src([
            `${fromSrc}/**/*.txt`
        ], {
        }).pipe(dest(`${toDist}/`))
    }

    return copyExamples;
}