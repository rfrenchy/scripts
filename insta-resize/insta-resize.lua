
-- create c bindings to the functions i need from imagemagick (composite, convert, height, width)
-- http://luajit.org/ext_ffi.html

local ffi = require("ffi")

ffi.cdef([[ 
    typedef void MagickWand;
    typedef void PixelWand;

    typedef int MagickBooleanType;
    typedef int ExceptionType;
    typedef int ssize_t;
    typedef int CompositeOperator;
    

    void MagickWandGenesis();
    MagickWand* NewMagickWand();

    char* MagickGetException(const MagickWand*, ExceptionType*);

    int MagickGetImageWidth(MagickWand*);
    int MagickGetImageHeight(MagickWand*);

    MagickBooleanType MagickCompositeImage(MagickWand *wand,
        const MagickWand *source_wand,const CompositeOperator compose,
        const ssize_t x,const ssize_t y);

    MagickBooleanType MagickScaleImage(MagickWand *wand,
        const size_t columns,const size_t rows);
]])


-- object for creating a square image for instagram
local square = {
    -- return a 1:1 dimension string of image
    dimension = function (width, height)
        -- use whatever measurement is biggest  
        local d = height > width and height or width;
        -- create 1:1 string of biggest measurement e.g. 1230x1230
        return d
    end,

    -- return instagram specific 1:1 measurement 
    instasize = function () return "1080x1080" end
}

-- object for creating portrait sized images for instagram
local portrait = {
    -- return a 4:5 dimension string of image
    dimension = function (height, width)   
        local wx = (height / 5) * 4 -- new width
        return string.gsub("%sx" .. height, "%s", wx)
    end,
    -- return instagram specific portrait size 
    instasize = function () return "1080x1350" end
}

local landscape = {
    dimension = function () return "" end,
    instasize = function () return "" end
}


-- local magick = require "magick.gmwand"


-- local img = assert(magick.load_image(arg[1]))
 

print "test"

-- local x = square.dimension(img:get_height(), img:get_width())





-- magick.load_image.blank_image(x, x, "white")

-- print(img)

-- local p = img:blank_image(x, x, "white")

-- print(x)
-- print(square.dimension(200, 199))