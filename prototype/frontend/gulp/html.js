import { src, dest } from "gulp";
import panini from "panini";
import plumber from "gulp-plumber";
import flatten from "gulp-flatten";

export function configureBuildHtmlTask({
    fromSrc,
    toDist,
    paniniOptions,
    continuePipe = pipeline => pipeline,
}) {
    function buildHtml() {
        panini.refresh();

        const bodyPipe =
            src(`${fromSrc}/*/*.html`)
                .pipe(plumber())
                .pipe(panini(paniniOptions))
                .pipe(flatten())
                .pipe(dest(`${toDist}/`));

        return continuePipe(bodyPipe);
    }

    return buildHtml;
}