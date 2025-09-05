# OpenListMount SPK Builder

## Build Requirements
- Linux/macOS environment
- GNU tar
- bash shell

## Usage

### GitHub Actions
1. Push code to main branch triggers auto-build
2. Artifacts will be available in Actions tab
3. Create release to auto-attach SPK file

### Local Build
```bash
chmod +x build.sh
./build.sh
```

## File Structure
```
src/
  |- scripts/       # Service control scripts
  |- webapi/        # Web interface files
  |- conf/          # Configuration templates
package/            # Temporary build dir
OpenListMount.spk   # Output package
```
