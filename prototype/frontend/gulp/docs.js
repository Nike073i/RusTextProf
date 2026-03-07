import gulpMarkdown from "gulp-markdown";
import through from "through2";
import { src, dest, series } from "gulp";
import rename from "gulp-rename";
import panini from "panini";

export function configureCreateDocsTask({
    fromSrc,
    toDist,
    paniniOptions
}) {

    function copyAssets() {
        return src([
            `${fromSrc}/**/*.{jpg,jpeg,png,gif,svg,bmp,ico,mp4,webm,ogg}`
        ], {
            encoding: false
        }).pipe(dest(toDist))
    }

    function convertMd() {
        panini.refresh();
        return src(`${fromSrc}/**/*.md`)
            .pipe(gulpMarkdown())
            .pipe(through.obj(function (file, enc, cb) {
                const content = file.contents.toString();

                const properties = "---\nlayout: docs\ntitle: О модели\n---\n";

                const newContent = `${properties}<div class="article">${content}</div>`;

                file.contents = Buffer.from(newContent);

                this.push(file);
                cb();
            }))
            .pipe(rename({
                basename: 'index',
            }))
            .pipe(panini(paniniOptions))
            .pipe(dest(toDist));
    }

    return series(copyAssets, convertMd);
}
