from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef(
    """
typedef unsigned char	FcChar8;
typedef unsigned short	FcChar16;
typedef unsigned int	FcChar32;
typedef bool FcBool;
typedef ... FcConfig;
typedef ... FcObjectSet;
typedef ... FcPattern;
typedef struct _FcFontSet {
    int		nfont;
    int		sfont;
    FcPattern	**fonts;
} FcFontSet;

typedef enum _FcResult {
    FcResultMatch, FcResultNoMatch, FcResultTypeMismatch, FcResultNoId,
    FcResultOutOfMemory
} FcResult;
typedef enum _FcMatchKind {
    FcMatchPattern, FcMatchFont, FcMatchScan,
    FcMatchKindEnd,
    FcMatchKindBegin = FcMatchPattern
} FcMatchKind;

static char *const FC_FAMILY;
static char *const FC_STYLE;
static char *const FC_FILE;

FcBool FcInit(void);
void FcFini(void);
FcConfig * FcConfigCreate(void);
void FcConfigDestroy(FcConfig *config);
FcBool FcConfigSetCurrent(FcConfig *config);
FcBool FcConfigAppFontAddFile(FcConfig *config, const FcChar8 *file);
FcBool FcConfigAppFontAddDir(FcConfig *config, const FcChar8 *dir);
void FcConfigAppFontClear(FcConfig *config);

FcPattern * FcNameParse(const FcChar8 *name);
FcBool FcConfigSubstitute(FcConfig *config, FcPattern *p, FcMatchKind kind);
void FcDefaultSubstitute(FcPattern *pattern);

FcFontSet * FcFontSetCreate(void);
FcObjectSet * FcObjectSetBuild (const char *first, ...);
FcFontSet * FcFontSort(
    FcConfig *config, FcPattern *p, FcBool trim, void *csp, FcResult *result);
FcPattern * FcFontRenderPrepare(FcConfig *config, FcPattern *pat, FcPattern *font);
FcBool FcFontSetAdd(FcFontSet *s, FcPattern *font);
void FcFontSetDestroy(FcFontSet *s);
void FcPatternDestroy(FcPattern *p);
FcPattern * FcPatternFilter(FcPattern *p, const FcObjectSet *os);
FcResult FcPatternGetString(FcPattern *p, const char *object, int n, FcChar8 **s);
void FcObjectSetDestroy(FcObjectSet *os);
"""
)

ffibuilder.set_source(
    "meson_python_cffi_example._fontconfig",
    """
#include <fontconfig/fontconfig.h>
""",
)
