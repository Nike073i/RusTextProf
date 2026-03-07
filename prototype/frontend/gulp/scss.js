import { src, dest } from "gulp";
import panini from "panini";
import plumber from "gulp-plumber";
import flatten from "gulp-flatten";
import gulpSass from "gulp-sass";
import * as dartSass from "sass";

const sass = gulpSass(dartSass);


export function configureBuildCssTask({
    mainStyleSrc,
    pageStylesSrc,
    toDist,
    continuePipe = pipeline => pipeline,
}) {
    function builCss() {
        panini.refresh();

        const bodyPipe =
            src([mainStyleSrc, `${pageStylesSrc}/*/*.scss`])
                .pipe(plumber())
                .pipe(sass())
                .pipe(flatten())
                .pipe(dest(`${toDist}/`));

        return continuePipe(bodyPipe);
    }

    return builCss;
}