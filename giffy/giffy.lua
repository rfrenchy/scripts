
-- create c bindings to the functions i need from imagemagick 
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
